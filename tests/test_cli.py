import unittest
from unittest.mock import patch, MagicMock
from kustomap.cli import parse_data, parse_headers, main
import sys
import io

class TestCLI(unittest.TestCase):

    def test_parse_data(self):
        self.assertEqual(parse_data("a=1&b=2"), {"a": "1", "b": "2"})
        self.assertEqual(parse_data(""), {})
        self.assertEqual(parse_data(None), {})

    def test_parse_headers(self):
        self.assertEqual(parse_headers(["User-Agent: test", "Accept: */*"]), {"User-Agent": "test", "Accept": "*/*"})
        self.assertEqual(parse_headers([]), {})
        self.assertEqual(parse_headers(None), {})

    @patch('kustomap.cli.Kustomap')
    def test_main(self, MockKustomap):
        # Mock scanner instance
        mock_scanner = MockKustomap.return_value
        mock_scanner.scan.return_value = [{"param": "id", "payload": "'", "method": "GET"}]

        # Capture stdout
        captured_output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            with patch.object(sys, 'argv', ["kustomap", "http://example.com?id=1"]):
                main()
        finally:
            sys.stdout = original_stdout

        output = captured_output.getvalue()
        self.assertIn("Scanning http://example.com?id=1", output)
        self.assertIn("Vulnerabilities found", output)
        self.assertIn("Parameter: id", output)

    @patch('kustomap.cli.Kustomap')
    def test_main_no_vulns(self, MockKustomap):
        mock_scanner = MockKustomap.return_value
        mock_scanner.scan.return_value = []

        captured_output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            with patch.object(sys, 'argv', ["kustomap", "http://example.com"]):
                main()
        finally:
             sys.stdout = original_stdout

        output = captured_output.getvalue()
        self.assertIn("No vulnerabilities found", output)
