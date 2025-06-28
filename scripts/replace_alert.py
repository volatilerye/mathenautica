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
        p = tag.find("p")
        if p:
            matched = re.match(
                r"<p>\[\!(default|note|tip|important|warning|caution|proof)\]\s*([^\n]*)",
                str(p),
                flags=re.IGNORECASE | re.MULTILINE,
            )
            if matched:
                # alert
                alert_type = matched.group(1).lower()
                match alert_type:
                    case "default":
                        tag.name = "div"
                        tag["class"] = "alert default"
                    case "note":
                        tag.name = "div"
                        tag["class"] = "alert note"
                    case "tip":
                        tag.name = "div"
                        tag["class"] = "alert tip"
                    case "important":
                        tag.name = "div"
                        tag["class"] = "alert important"
                    case "warning":
                        tag.name = "div"
                        tag["class"] = "alert warning"
                    case "caution":
                        tag.name = "div"
                        tag["class"] = "alert caution"
                    case "proof":
                        tag.name = "div"
                        tag["class"] = "alert proof"
                    case _:
                        continue
                # title
                title = matched.group(2)
                context = str(p)[matched.span()[1] : -4]
                if title:
                    match alert_type:
                        case "default":
                            tag.string = (
                                f"<p class='alert title'>{title}</p>\n{context}</p>\n"
                            )
                        case "note":
                            tag.string = f"<p class='alert note title'>{title}</p>\n{context}</p>\n"
                        case "tip":
                            tag.string = f"<p class='alert tip title'>{title}</p>\n{context}</p>\n"
                        case "important":
                            tag.string = f"<p class='alert important title'>{title}</p>\n{context}</p>\n"
                        case "warning":
                            tag.string = f"<p class='alert warning title'>{title}</p>\n{context}</p>\n"
                        case "caution":
                            tag.string = f"<p class='alert caution title'>{title}</p>\n{context}</p>\n"
                        case "proof":
                            begin_details = (
                                "<details><summary>証明 (クリックで展開)</summary>"
                            )
                            end_details = "</details>"
                            end_proof = '<div style="position: relative;"><span style="position: absolute; right: 0em; bottom: 0em; font-size: 1.5em">■</span></div>'
                            tag.string = f"{begin_details}\n\n<p class='alert proof title'>{title}</p>\n{context}\n{end_proof}</p>\n{end_details}\n"
                        case _:
                            continue

    with html.open("w", encoding="utf-8") as f:
        f.write(soup.encode(formatter=None).decode("utf-8"))


if __name__ == "__main__":
    for html_path in BASE_HTML_DIR.glob("**/*.html"):
        replace_alerts_in_md_files(html_path)
