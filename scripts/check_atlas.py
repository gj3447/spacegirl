#!/usr/bin/env python3
"""Validate the local, source-navigation-only Spacegirl research atlas."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "METAHUMOTONIC/SPACEGIRL/"
NAMESPACE = "spacegirl:"


def fail(message: str) -> None:
    raise ValueError(message)


def load(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    content = load(ROOT / "APOSTLE_CONTENT.json")
    atlas = load(ROOT / "graph" / "research-atlas.json")
    expected = {item["repository_path"]: item for item in content["documents"]
                if item["source_path"].startswith(PREFIX)}
    if len(expected) != 37:
        fail(f"expected 37 source documents, got {len(expected)}")
    if atlas.get("schema") != "spacegirl/research-atlas/2" or atlas.get("scope") != "SOURCE_NAVIGATION_ONLY":
        fail("schema or scope is invalid")
    if atlas.get("source_set", {}).get("document_count") != len(expected):
        fail("source-set document count mismatch")

    node_by_uid = {}
    for node in atlas.get("nodes", []):
        uid = node.get("uid")
        if not isinstance(uid, str) or not uid.startswith(NAMESPACE) or uid in node_by_uid:
            fail(f"invalid or duplicate node UID: {uid!r}")
        node_by_uid[uid] = node
    sources = [node for node in node_by_uid.values() if node.get("kind") == "SourceArtifact"]
    for node in sources:
        path = node.get("repository_path")
        if not isinstance(path, str):
            fail("source artifact repository_path is missing")
        candidate = ROOT / path
        try:
            candidate.resolve().relative_to(ROOT.resolve())
        except ValueError:
            fail(f"{path}: source path escapes repository root")
        if not path.startswith("sources/"):
            fail(f"{path}: source artifact must stay below sources/")
    source_by_path = {node.get("repository_path"): node for node in sources}
    if len(sources) != len(expected) or set(source_by_path) != set(expected):
        fail("source artifacts do not exactly match the 37 pinned documents")
    for path, item in expected.items():
        node = source_by_path[path]
        for key in ("source_path", "source_repository", "source_revision", "sha256", "bytes"):
            if node.get(key) != item.get(key):
                fail(f"{path}: {key} differs from APOSTLE_CONTENT.json")
        if (node.get("authority"), node.get("content_authority")) != ("SOURCE_DOCUMENT", "UNSPECIFIED"):
            fail(f"{path}: invalid source authority boundary")
        data = (ROOT / path).read_bytes()
        if len(data) != node["bytes"] or hashlib.sha256(data).hexdigest() != node["sha256"]:
            fail(f"{path}: local bytes do not match pin")

    predicates = {item.get("uid"): item for item in atlas.get("vocabulary", {}).get("predicates", [])}
    if not predicates:
        fail("predicate vocabulary missing")
    for uid, predicate in predicates.items():
        if not isinstance(uid, str) or not uid.startswith(NAMESPACE):
            fail(f"predicate UID invalid: {uid!r}")
        if not predicate.get("domain") or not predicate.get("range") or not predicate.get("cardinality"):
            fail(f"{uid}: domain/range/cardinality missing")
        if predicate.get("direction") not in {"forward", "bidirectional"}:
            fail(f"{uid}: direction invalid")

    edge_uids = set()
    for edge in atlas.get("edges", []):
        uid = edge.get("uid")
        if not isinstance(uid, str) or not uid.startswith(NAMESPACE) or uid in edge_uids:
            fail(f"invalid or duplicate edge UID: {uid!r}")
        edge_uids.add(uid)
        predicate = predicates.get(edge.get("predicate"))
        source, target = node_by_uid.get(edge.get("from")), node_by_uid.get(edge.get("to"))
        if not predicate or not source or not target:
            fail(f"{uid}: unknown predicate or endpoint")
        if source.get("kind") not in predicate["domain"] or target.get("kind") not in predicate["range"]:
            fail(f"{uid}: endpoint types violate predicate contract")

    claims = [node for node in node_by_uid.values() if node.get("kind") == "Claim"]
    for claim in claims:
        if claim.get("authority") not in {"SOURCE_DOCUMENT", "SECONDARY_AI"} or not claim.get("status"):
            fail(f"{claim['uid']}: claim provenance/status missing")
        if claim["authority"] == "SECONDARY_AI" and claim["status"] != "NAVIGATION_ONLY":
            fail(f"{claim['uid']}: AI interpretation must be NAVIGATION_ONLY")
        for anchor in claim.get("source_anchors", []):
            source = node_by_uid.get(anchor.get("source"))
            if not source or source.get("kind") != "SourceArtifact" or not anchor.get("anchor") or not anchor.get("quote"):
                fail(f"{claim['uid']}: source anchor invalid")
            source_text = (ROOT / source["repository_path"]).read_text(encoding="utf-8")
            if anchor["quote"] not in source_text:
                fail(f"{claim['uid']}: quoted evidence is absent from {source['repository_path']}")
        if not claim.get("source_anchors"):
            fail(f"{claim['uid']}: source anchors missing")

    required = {"spacegirl:direction:ssb", "spacegirl:direction:we-flying-up",
                "spacegirl:claim:v2-draft-not-ratified", "spacegirl:claim:grammar-draft-not-ratified",
                "spacegirl:claim:open-boundary-status", "spacegirl:gap:primary-mind-texts"}
    if missing := required - set(node_by_uid):
        fail(f"competency-query anchors missing: {', '.join(sorted(missing))}")
    for direction in ("spacegirl:direction:ssb", "spacegirl:direction:we-flying-up"):
        if not any(edge["to"] == direction for edge in atlas["edges"]):
            fail(f"CQ failure: {direction} is not source-linked")
    if node_by_uid["spacegirl:entity:persona"].get("stable_entity_uid") != content_identity():
        fail("CQ failure: persona does not reuse the existing identity")
    for name, origin, destination in (("ssb", "network", "sexvoid"),
                                     ("we-flying-up", "sexvoid", "network")):
        direction = "spacegirl:direction:" + name
        for predicate, expected_region in (("HAS_ORIGIN", origin), ("HAS_DESTINATION", destination)):
            links = [edge for edge in atlas["edges"]
                     if edge["from"] == direction and edge["predicate"] == "spacegirl:predicate:" + predicate]
            if len(links) != 1 or links[0]["to"] != "spacegirl:region:" + expected_region:
                fail(f"CQ failure: {name} {predicate} direction/cardinality changed")
            claim = node_by_uid.get(links[0].get("claim"), {})
            if claim.get("kind") != "Claim" or not claim.get("source_anchors"):
                fail("direction edge lacks an evidence-backed claim")
    print(json.dumps({"ok": True, "sources": len(sources), "claims": len(claims), "edges": len(edge_uids)}, ensure_ascii=False))
    return 0


def content_identity() -> str:
    return load(ROOT / "APOSTLE_MODULE.json")["identity"]["stable_entity_uid"]


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"atlas check failed: {error}", file=sys.stderr)
        raise SystemExit(1)
