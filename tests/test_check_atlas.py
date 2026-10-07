"""Regression tests for adversarial changes to the checked atlas artifact."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AtlasCheckerTest(unittest.TestCase):
    def fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        copied = Path(temporary.name) / "spacegirl"
        copied.mkdir()
        shutil.copy2(ROOT / "APOSTLE_CONTENT.json", copied / "APOSTLE_CONTENT.json")
        shutil.copy2(ROOT / "APOSTLE_MODULE.json", copied / "APOSTLE_MODULE.json")
        shutil.copytree(ROOT / "sources", copied / "sources")
        shutil.copytree(ROOT / "graph", copied / "graph")
        (copied / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts" / "check_atlas.py", copied / "scripts" / "check_atlas.py")
        return temporary, copied

    def checked(self, copied: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/check_atlas.py"], cwd=copied,
            text=True, capture_output=True, check=False,
        )

    def mutate(self, copied: Path, callback) -> None:
        graph_path = copied / "graph" / "research-atlas.json"
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        callback(graph)
        graph_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def test_baseline_graph_passes(self) -> None:
        temporary, copied = self.fixture()
        with temporary:
            result = self.checked(copied)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_forged_claim_quote(self) -> None:
        temporary, copied = self.fixture()
        with temporary:
            self.mutate(copied, lambda graph: next(node for node in graph["nodes"] if node["kind"] == "Claim")["source_anchors"][0].update({"quote": "forged evidence"}))
            result = self.checked(copied)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("quoted evidence is absent", result.stderr)

    def test_rejects_unknown_edge_endpoint(self) -> None:
        temporary, copied = self.fixture()
        with temporary:
            self.mutate(copied, lambda graph: graph["edges"][0].update({"to": "spacegirl:direction:invented"}))
            result = self.checked(copied)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown predicate or endpoint", result.stderr)

    def test_rejects_source_path_escape(self) -> None:
        temporary, copied = self.fixture()
        with temporary:
            self.mutate(copied, lambda graph: next(node for node in graph["nodes"] if node["kind"] == "SourceArtifact").update({"repository_path": "../APOSTLE_MODULE.json"}))
            result = self.checked(copied)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("source path escapes repository root", result.stderr)

    def test_rejects_reversed_ssb_direction(self) -> None:
        temporary, copied = self.fixture()
        with temporary:
            self.mutate(copied, lambda graph: next(edge for edge in graph["edges"]
                if edge["uid"] == "spacegirl:edge:ssb-has_origin").update({"to": "spacegirl:region:sexvoid"}))
            result = self.checked(copied)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("direction/cardinality changed", result.stderr)

    def test_rejects_duplicate_origin(self) -> None:
        temporary, copied = self.fixture()
        with temporary:
            def duplicate(graph):
                edge = dict(next(edge for edge in graph["edges"] if edge["uid"] == "spacegirl:edge:ssb-has_origin"))
                edge["uid"] += "-duplicate"
                graph["edges"].append(edge)
            self.mutate(copied, duplicate)
            result = self.checked(copied)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("direction/cardinality changed", result.stderr)


if __name__ == "__main__":
    unittest.main()
