import re
import os
from pathlib import Path
from typing import Final

from bs4 import BeautifulSoup

BASE_HTML_DIR: Final[Path] = Path("../html")


def replace_alerts_in_md_files(html: Path) -> None:
    with html.open(encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    for tag in soup.find_all("blockquote"):
        matched: re.Match[str] | None = None
        if p := tag.find("p") is not None:
            matched = re.fullmatch(
                str(p),
                r"\[\!(default|note|tip|important|warning|caution)\]\s*([^\n]*)(.*)",
                flags=re.IGNORECASE,
            )
            if matched:
                # alert
                alert_type = matched.group(1).lower()
                match alert_type:
                    case "default":
                        tag.name = "div"
                    case "note":
                        tag.name = "div"
                    case "tip":
                        tag.name = "div"
                    case "important":
                        tag.name = "div"
                    case "warning":
                        tag.name = "div"
                    case "caution":
                        tag.name = "div"
                    case _:
                        continue

                # title
                title = matched.group(2)
                content = matched.group(3)
                if title:
                    match alert_type:
                        case "default":
                            tag.name = f"<p class='alert title'>{title}</p>\n{content}"
                        case "note":
                            tag.name = (
                                f"<p class='alert note title'>{title}</p>\n{content}"
                            )
                        case "tip":
                            tag.name = (
                                f"<p class='alert tip title'>{title}</p>\n{content}"
                            )
                        case "important":
                            tag.name = f"<p class='alert important title'>{title}</p>\n{content}"
                        case "warning":
                            tag.name = (
                                f"<p class='alert warning title'>{title}</p>\n{content}"
                            )
                        case "caution":
                            tag.name = (
                                f"<p class='alert caution title'>{title}</p>\n{content}"
                            )
                        case _:
                            continue


if __name__ == "__main__":
    for html_path in BASE_HTML_DIR.glob("**/*.html"):
        replace_alerts_in_md_files(html_path)
