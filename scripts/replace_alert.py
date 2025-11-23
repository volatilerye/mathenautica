import re
from typing import Final

from bs4 import BeautifulSoup

alert_tags: Final[set] = {
    # custom alert: default quotation
    "default",
    # github flavor markdown alert
    "info",  # renamed from 'note' to conflict with math alert
    "tip",
    "important",
    "warning",
    "caution",
    # custom alert: for mathenautics
    "proof",
    "proof-without-details",
    "theorem",
    "lemma",
    "proposition",
    "corollary",
    "conjecture",
    "criterion",
    "assertion",
    "definition",
    "example",
    "exercise",
    "condition",
    "problem",
    "algorithm",
    "question",
    "axiom",
    "property",
    "assumption",
    "hypothesis",
    "remark",
    "note",
    "case",
    "notation",
    "claim",
    "summary",
    "acknowledgment",
    "conclusion",
}


def replace_alerts_in_md_files(html_text: str) -> str:
    soup = BeautifulSoup(html_text, "html.parser")

    for tag in soup.find_all("blockquote"):
        matched: re.Match[str] | None = None
        p = tag.find("p")
        if p:
            matched = re.match(
                rf"<p>\[\!({'|'.join(alert_tags)})\] *(.*)",
                str(p).split("\n")[0],
                flags=re.IGNORECASE,
            )
            if matched:
                # alert
                alert_type = matched.group(1).lower()
                if alert_type in alert_tags:
                    tag.name = "div"
                    tag["class"] = f"alert {alert_type}"
                else:
                    continue
                # title
                title = matched.group(2)
                context = "\n".join(
                    str(tag)
                    .replace(f'<div class="{tag["class"]}">\n', "")
                    .replace("\n</div>", "", count=1)
                    .split("\n", 1)[1:]
                )
                if tag["class"]:
                    match alert_type:
                        case "default":
                            tag.string = (
                                f"<p class='alert title'>{title}</p>\n{context}</p>\n"
                            )
                        case "proof":
                            begin_details = (
                                "<details><summary><b>証明</b> (クリックで展開)</summary>"
                            )
                            end_details = "</details>"
                            end_proof = '<div style="text-align: right;"><span style="font-size: 1.5em;">■</span></div>'
                            if title != "":
                                tag.string = f"{begin_details}\n\n<p class='alert proof title'>{title}</p>\n<p>\n{context}</p>\n{end_proof}\n{end_details}\n"
                            else:
                                tag.string = f"{begin_details}\n\n<p>\n{context}</p>\n{end_proof}\n{end_details}\n"
                        case "proof-without-details":
                            end_proof = '<div style="text-align: right;"><span style="font-size: 1.5em;">■</span></div>'
                            tag.string = f"<p class='alert {alert_type} title'>{title}</p>\n{context}{end_proof}\n</p>\n"

                                              
                        case _:
                            tag.string = f"<p class='alert {alert_type} title'>{title}</p>\n{context}</p>\n"

    return soup.encode(formatter=None).decode("utf-8")