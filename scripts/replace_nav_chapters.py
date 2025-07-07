import os
from pathlib import Path

from bs4 import BeautifulSoup


def replace_navigation(
    html_text: str, html_path: Path, index: int, toc_list: list[tuple[str, Path]]
) -> str:
    # remove default navigation
    soup = BeautifulSoup(html_text, "html.parser")
    for tag in soup.find_all("nav", class_="nav-wrapper"):
        tag.decompose()

    # add custom navigation
    navigation: str = ""
    if index > 0:
        navigation += '<nav class="prev-next-buttons" aria-label="Page navigation">'
        prev_title, prev_html_path = toc_list[index - 1]
        prev_html_path = os.path.relpath(prev_html_path, start=html_path.parent)
        navigation += f"""
            <a class="local-button-active" href="{prev_html_path}" rel="prev" title="{prev_title}" style="text-decoration: none;" aria-keyshortcuts="Left">
                <span class="arrow">←</span>
                <span class="where">{prev_title}</span>
            </a>
        """
    if index < len(toc_list) - 1:
        next_title, next_html_path = toc_list[index + 1]
        next_html_path = os.path.relpath(next_html_path, start=html_path.parent)
        navigation += f"""
            <a class="local-button-active" href="{next_html_path}" rel="next" title="{next_title}" style="text-decoration: none;" aria-keyshortcuts="Right">
            <span class="where">{next_title}</span>
            <span class="arrow">→</span>
            </a>
        """
    navigation += "</nav>"

    main = soup.find("main")
    if main:
        inner_main = str(main).replace("<main>", "").replace("</main>", "")
        new_main = f"{navigation}\n{inner_main}\n{navigation}"
        main.clear()
        main.append(BeautifulSoup(new_main, "html.parser"))

    return soup.encode(formatter=None).decode("utf-8")
