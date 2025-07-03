import re
from pathlib import Path
from typing import Final

BASE_HTML_DIR: Final[Path] = Path("../html")


def replace_book_to_site(html: Path) -> None:
    with html.open(encoding="utf-8") as f:
        replaced = f.read().replace(
            '<h1 class="menu-title">',
            '<h1 class="custom-menu-title">',
        )

    with html.open("w", encoding="utf-8") as f:
        f.write(replaced)


def invert_e(html: Path) -> None:
    with html.open(encoding="utf-8") as f:
        replaced = re.sub(
            r"MATHENAUTICA(?!\</title\>)(.*)",
            r'MATH<div class="invert-e">E</div>NAUTICA\1',
            f.read(),
        )

    with html.open("w", encoding="utf-8") as f:
        f.write(replaced)


if __name__ == "__main__":
    for html in BASE_HTML_DIR.glob("**/*.html"):
        replace_book_to_site(html)
        invert_e(html)
