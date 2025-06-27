import re
import os
from pathlib import Path
from typing import Final

from bs4 import BeautifulSoup

def get_toc_list() -> list[tuple[str, Path]]:
    with Path("../../src/SUMMARY.md").open("r", encoding="utf-8") as file:
        matched = re.findall(r"\[(.+)\]\((.+\.md)\)", file.read())
    return [(title, Path(path)) for title, path in matched]

BASE_HTML_DIR: Final[Path] = Path("../html")
TOC_LIST: list[tuple[str, Path]] = get_toc_list()


def replace_navigation(index: int, md_path: Path) -> None:
    html_path = BASE_HTML_DIR / md_path.parent / (md_path.stem + ".html")

    # remove default navigation
    with html_path.open("r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        for tag in soup.find_all("nav", class_="nav-wrapper"):
            tag.decompose()
        # for tag in soup.find_all("nav", class_="nav-wide-wrapper"):
        #     tag.decompose()

    # add custom navigation
    navigation: str = '<nav class="prev-next-buttons" aria-label="Page navigation">'
    if index > 0:
        prev_title, prev_md_path = TOC_LIST[index - 1]
        prev_html_path = os.path.relpath(
            (BASE_HTML_DIR / prev_md_path.parent / (prev_md_path.stem + ".html")),
            start=html_path.parent,
        )
        navigation += f"""
            <a class="local-button active" href="{prev_html_path}" rel="prev" title="{prev_title}" style="text-decoration: none;" aria-keyshortcuts="Left">
                <span class="arrow">←</span>
                <span class="where">{prev_title}</span>
            </a>
        """
    if index < len(TOC_LIST) - 1:
        next_title, next_md_path = TOC_LIST[index + 1]
        next_html_path = os.path.relpath(
            (BASE_HTML_DIR / next_md_path.parent / (next_md_path.stem + ".html")),
            start=html_path.parent,
        )
        navigation += f"""
            <a class="local-button active" href="{next_html_path}" rel="next" title="{next_title}" style="text-decoration: none;" aria-keyshortcuts="Right">
                <span class="where">{next_title}</span>
                <span class="arrow">→</span>
            </a>
        """
    navigation += "</nav>"

    main = soup.find("main")
    if main:
        inner_main = str(main).replace('<main>', '').replace('</main>', '')
        new_main = f"{navigation}\n{inner_main}\n{navigation}"
        main.clear()
        main.append(BeautifulSoup(new_main, "html.parser"))

    with html_path.open("w", encoding="utf-8") as f:
        f.write(soup.encode(formatter=None).decode("utf-8"))

if __name__ == "__main__":
    for index, (title, md_path) in enumerate(TOC_LIST):
        replace_navigation(index, md_path)
        
    replace_navigation(0, BASE_HTML_DIR / 'index.html')  # index.html