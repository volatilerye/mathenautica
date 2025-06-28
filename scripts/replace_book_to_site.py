from pathlib import Path
from typing import Final


BASE_HTML_DIR: Final[Path] = Path("../html")


def replace_book_to_site(html: Path) -> None:
    with html.open(encoding="utf-8") as f:
        replaced = (
            f.read()
            .replace(
                " to search in the book",
                " to search in the site",
            )
            .replace("Search this book ...", "Search this site ...")
        )

    with html.open("w", encoding="utf-8") as f:
        f.write(replaced)


if __name__ == "__main__":
    for html in BASE_HTML_DIR.glob("**/*.html"):
        replace_book_to_site(html)
