import re
import os
from pathlib import Path
from typing import Final

from bs4 import BeautifulSoup

BASE_HTML_DIR: Final[Path] = Path('../html')

def get_toc_list() -> list[tuple[str, Path]]:
    with Path("../../src/SUMMARY.md").open("r", encoding="utf-8") as file:
        matched = re.findall(r"\[(.+)\]\((.+\.md)\)", file.read())
    return [(title, Path(path)) for title, path in matched]

if __name__ == "__main__":
    toc_list = get_toc_list()
    for i, (title, md_path) in enumerate(toc_list):
        html_path = BASE_HTML_DIR / md_path.parent / (md_path.stem + '.html')
        
        # remove default navigation
        with html_path.open('r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            for tag in soup.find_all('nav', class_="nav-wrapper"):
                tag.decompose()
            for tag in soup.find_all('nav', class_="nav-wide-wrapper"):
                tag.decompose()
        
        # add custom navigation
        navigation: str = '<nav class="prev-next-buttons">'
        if i > 0:
            prev_title, prev_md_path = toc_list[i - 1]
            print(BASE_HTML_DIR / prev_md_path.parent / (prev_md_path.stem + '.html'))
            print(html_path)
            prev_html_path = os.path.relpath((BASE_HTML_DIR / prev_md_path.parent / (prev_md_path.stem + '.html')), start=html_path.parent)
            print(prev_html_path)
            navigation += f"""
                <a class="local-button active" href="{prev_html_path}" rel="prev" title="{prev_title}" text-decoration="none">
                    <span class="arrow">←</span>
                    <span class="where">{prev_title}</span>
                </a>
            """
        if i < len(toc_list) - 1:
            next_title, next_md_path = toc_list[i + 1]
            next_html_path = os.path.relpath((BASE_HTML_DIR / next_md_path.parent / (next_md_path.stem + '.html')), start=html_path.parent)
            navigation += f"""
                <a class="local-button active" href="{next_html_path}" rel="next" title="{next_title}" text-decoration="none">
                    <span class="where">{next_title}</span>
                    <span class="arrow">→</span>
                </a>
            """
        navigation += '</nav>'

        main = soup.find('main')
        new_main = f'{navigation}\n{str(soup.find('main'))}\n{navigation}'
        main.clear()
        main.append(BeautifulSoup(new_main, 'html.parser'))
        
        with html_path.open('w', encoding='utf-8') as f:
            f.write(soup.encode(formatter=None).decode('utf-8'))

