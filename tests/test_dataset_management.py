"""Testes da CLI e do catálogo, sem executar o Merge sort."""

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from dataset_io.catalog import DatasetCatalog
from dataset_io.cli import main
from dataset_io.errors import DatasetCatalogError


class DatasetManagementCliTests(unittest.TestCase):
    def run_cli(self, *arguments: str) -> tuple[int, str, str]:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            exit_code = main(list(arguments))
        return exit_code, stdout.getvalue(), stderr.getvalue()

    def test_legacy_mode_remains_compatible(self) -> None:
        exit_code, output, error = self.run_cli(
            "datasets/validos/iris_petal_length.txt",
            "--format",
            "text",
            "--type",
            "float",
            "--sample",
            "3",
        )

        self.assertEqual(exit_code, 0)
        self.assertIn("Quantidade: 15", output)
        self.assertIn("Amostra: [1.4, 4.7, 6.0]", output)
        self.assertEqual(error, "")

    def test_list_text_contains_all_catalog_categories(self) -> None:
        exit_code, output, error = self.run_cli("datasets", "list")

        self.assertEqual(exit_code, 0)
        self.assertIn("V01", output)
        self.assertIn("I01", output)
        self.assertIn("E02", output)
        self.assertIn("válida", output)
        self.assertIn("inválida", output)
        self.assertIn("externa", output)
        self.assertEqual(error, "")

    def test_list_json_has_stable_catalog_shape(self) -> None:
        exit_code, output, error = self.run_cli(
            "datasets",
            "list",
            "--output",
            "json",
        )

        document = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(document["catalog_version"], 1)
        self.assertEqual(len(document["datasets"]), 15)
        self.assertEqual(
            {entry["category"] for entry in document["datasets"]},
            {"valid", "invalid", "external"},
        )
        self.assertEqual(error, "")

    def test_inspect_valid_dataset(self) -> None:
        exit_code, output, error = self.run_cli(
            "datasets",
            "inspect",
            "V01",
            "--sample",
            "3",
            "--output",
            "json",
        )

        document = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(document["status"], "valid")
        self.assertEqual(document["count"], 15)
        self.assertEqual(document["sample"], [1.4, 4.7, 6.0])
        self.assertEqual(error, "")

    def test_inspect_csv_dataset(self) -> None:
        exit_code, output, error = self.run_cli(
            "datasets",
            "inspect",
            "V05",
            "--sample",
            "2",
            "--output",
            "json",
        )

        document = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(document["status"], "valid")
        self.assertEqual(document["format"], "csv")
        self.assertEqual(document["column"], "petal_length")
        self.assertEqual(document["sample"], [1.4, 4.7])
        self.assertEqual(error, "")

    def test_inspect_invalid_dataset_reports_without_crashing(self) -> None:
        exit_code, output, error = self.run_cli(
            "datasets",
            "inspect",
            "I01",
            "--output",
            "json",
        )

        document = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(document["status"], "invalid")
        self.assertIn("comparáveis", document["error"])
        self.assertEqual(error, "")

    def test_inspect_external_dataset_does_not_download(self) -> None:
        exit_code, output, error = self.run_cli(
            "datasets",
            "inspect",
            "E02",
            "--output",
            "json",
        )

        document = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertEqual(document["status"], "external")
        self.assertEqual(document["availability"], "external")
        self.assertIsNone(document["count"])
        self.assertEqual(error, "")

    def test_validate_uses_distinct_exit_codes(self) -> None:
        valid_code, _, _ = self.run_cli("datasets", "validate", "V01")
        invalid_code, _, _ = self.run_cli("datasets", "validate", "I01")
        external_code, _, _ = self.run_cli("datasets", "validate", "E02")
        unsupported_code, _, _ = self.run_cli("datasets", "validate", "V04")
        unknown_code, _, _ = self.run_cli("datasets", "validate", "UNKNOWN")

        self.assertEqual(valid_code, 0)
        self.assertEqual(invalid_code, 1)
        self.assertEqual(external_code, 2)
        self.assertEqual(unsupported_code, 2)
        self.assertEqual(unknown_code, 2)

    def test_validate_json_does_not_include_a_sample(self) -> None:
        exit_code, output, error = self.run_cli(
            "datasets",
            "validate",
            "V01",
            "--output",
            "json",
        )

        document = json.loads(output)
        self.assertEqual(exit_code, 0)
        self.assertIsNone(document["sample"])
        self.assertEqual(error, "")

    def test_catalog_rejects_duplicate_ids(self) -> None:
        document = {
            "version": 1,
            "datasets": [
                {
                    "id": "D01",
                    "name": "one",
                    "category": "external",
                    "source_url": "https://example.com/one",
                    "description": "one",
                    "managed": False,
                },
                {
                    "id": "D01",
                    "name": "two",
                    "category": "external",
                    "source_url": "https://example.com/two",
                    "description": "two",
                    "managed": False,
                },
            ],
        }

        with tempfile.TemporaryDirectory() as directory:
            catalog_path = Path(directory) / "catalog.json"
            catalog_path.write_text(json.dumps(document), encoding="utf-8")
            with self.assertRaises(DatasetCatalogError):
                DatasetCatalog.from_file(catalog_path, root=directory)

    def test_catalog_rejects_path_escape(self) -> None:
        document = {
            "version": 1,
            "datasets": [
                {
                    "id": "D01",
                    "name": "escape",
                    "category": "valid",
                    "format": "text",
                    "value_type": "text",
                    "path": "../outside.txt",
                    "description": "escape",
                    "managed": True,
                }
            ],
        }

        with tempfile.TemporaryDirectory() as directory:
            catalog_path = Path(directory) / "catalog.json"
            catalog_path.write_text(json.dumps(document), encoding="utf-8")
            with self.assertRaises(DatasetCatalogError):
                DatasetCatalog.from_file(catalog_path, root=directory)


if __name__ == "__main__":
    unittest.main()
