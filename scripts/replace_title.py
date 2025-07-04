import re
from pathlib import Path
from typing import Final

BASE_HTML_DIR: Final[Path] = Path("../html")
EXCLUDE_INVERT_E: Final[set[str]] = {
    '<meta content="MATHENAUTICA" property="og:site_name"/>',
    r'^<title>(.+) \- MATHENAUTICA</title>$'
}

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
        replaced = f.read()
        matched = re.finditer(r"^(.*)(MATHENAUTICA)(.*)$", replaced, flags = re.MULTILINE)
        for match in list(matched)[::-1]:
            for exclude in EXCLUDE_INVERT_E:
                if re.match(exclude, match.group(0)):
                    break
            else:
                replaced = replaced[:match.start(2)] + "MATH<div class='invert-e'>E</div>NAUTICA" + replaced[match.end(2):]

    with html.open("w", encoding="utf-8") as f:
        f.write(replaced)


if __name__ == "__main__":
    for html in BASE_HTML_DIR.glob("**/*.html"):
        replace_book_to_site(html)
        invert_e(html)
