"""Validate architecture guide content, evidence references and reader structure."""
from pathlib import Path
import json
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup


def main():
    root=Path(__file__).resolve().parents[1]
    source=root/"docs/iosd逆向分析教程.md"
    output=source.with_suffix(".html")
    soup=BeautifulSoup(output.read_text(encoding="utf-8"),"html.parser")
    sections=soup.select("section.chapter")
    nav=soup.select("li[data-nav] a")
    assert len(sections)==len(nav)==23
    assert not soup.select("details"),"Exercise/answer blocks must not return"
    ids=[node["id"] for node in soup.select("[id]")]
    assert len(ids)==len(set(ids)),"duplicate DOM identities"
    for link in soup.select("a[href]"):
        href=link["href"]
        parsed=urlsplit(href)
        if parsed.scheme or parsed.netloc:
            raise AssertionError("Textbook unexpectedly contains a remote link: "+href)
        if parsed.path:
            target=(output.parent/unquote(parsed.path)).resolve()
            assert target.is_file(),"missing local reference: "+str(target)
        if not parsed.path and parsed.fragment:
            assert unquote(parsed.fragment) in ids,"missing internal anchor"
    assert not soup.select("script[src],link[href],iframe,img[src]"),"unexpected external or embedded dependency"
    document=source.read_text(encoding="utf-8")
    assert not any(word in document for word in ("本章练习", "参考答案", "本章要解决的问题"))
    assert "iosd模块与子系统.md" in document
    paths=[json.loads(line) for line in (root/"reports/vpdn-activation-20261029/test-paths.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(paths)==19
    for row in paths:
        assert row["syntax_candidate"] in document,"missing reviewed VPDN template"
    manifest=json.loads(output.with_suffix(".manifest.json").read_text(encoding="utf-8"))
    assert manifest["chapter_count"]==16 and manifest["appendix_count"]==6
    assert not any(manifest[k] for k in ("ida_access","mcp_access","network_access"))
    assert manifest["answer_blocks"] == 0
    print("16 architecture sections, 6 appendices, no exercises/answers, all local references and 19 reviewed VPDN templates verified.")


if __name__=="__main__":main()
