import re
from pathlib import Path
from typing import Final

from replace_title import invert_e
from replace_head import replace_ogp
from replace_book_to_site import replace_book_to_site
from replace_alert import replace_alerts_in_md_files
from replace_nav_chapters import replace_navigation

# from fix_meta_tag import fix_meta_tag

def get_toc_list() -> list[tuple[str, Path]]:
    toc_list: list[tuple[str, Path]] = []
    with Path("../../src/SUMMARY.md").open("r", encoding="utf-8") as file:
        for title, path in re.findall(r"\[(.+)\]\((.+\.md)\)", file.read()):
            html_path = Path("../html") / Path(path).parent / (Path(path).stem + ".html")
            toc_list.append((title, html_path))
    return toc_list

TOC_LIST: list[tuple[str, Path]] = get_toc_list()
BASE_HTML_DIR: Final[Path] = Path("../html")

if __name__ == "__main__":
    for i, html_path in enumerate(BASE_HTML_DIR.glob("**/*.html")):
        with html_path.open("r", encoding="utf-8") as f:
            html_text = f.read()
        
        # Replace
        html_text = invert_e(html_text)
        html_text = replace_ogp(html_text, html_path)
        html_text = replace_book_to_site(html_text)
        html_text = replace_alerts_in_md_files(html_text)
        
        try:
            index: int = [t[1] for t in TOC_LIST].index(html_path)
            html_text = replace_navigation(html_text, html_path, index, TOC_LIST)
        except ValueError:  # 404.html
            pass


        # Write back the modified HTML
        with html_path.open("w", encoding="utf-8") as f:
            f.write(html_text)
            