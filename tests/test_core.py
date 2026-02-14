import unittest
from unittest.mock import patch, MagicMock
import requests
from kustomap.core import Kustomap

class TestKustomap(unittest.TestCase):

    def test_init(self):
        scanner = Kustomap("http://example.com")
        self.assertEqual(scanner.url, "http://example.com")
        self.assertEqual(scanner.method, "GET")
        self.assertEqual(scanner.headers, {})
        self.assertEqual(scanner.data, {})

    @patch('requests.get')
    def test_scan_get_vulnerable(self, mock_get):
        # Setup mock response for vulnerability
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "Syntax error"
        mock_get.return_value = mock_response

        scanner = Kustomap("http://example.com?id=1")
        vulns = scanner.scan()

        self.assertTrue(len(vulns) > 0)
        self.assertEqual(vulns[0]['param'], 'id')

    @patch('requests.get')
    def test_scan_get_not_vulnerable(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "OK"
        mock_get.return_value = mock_response

        scanner = Kustomap("http://example.com?id=1")
        vulns = scanner.scan()

        self.assertEqual(len(vulns), 0)

    @patch('requests.post')
    def test_scan_post_vulnerable_500(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_post.return_value = mock_response

        scanner = Kustomap("http://example.com", method="POST", data={"user": "admin"})
        vulns = scanner.scan()

        self.assertTrue(len(vulns) > 0)
        self.assertEqual(vulns[0]['param'], 'user')

    @patch('requests.get')
    def test_scan_get_no_params(self, mock_get):
        scanner = Kustomap("http://example.com")
        vulns = scanner.scan()
        self.assertEqual(len(vulns), 0)
        mock_get.assert_not_called()

    @patch('requests.post')
    def test_scan_post_no_data(self, mock_post):
        scanner = Kustomap("http://example.com", method="POST")
        vulns = scanner.scan()
        self.assertEqual(len(vulns), 0)
        mock_post.assert_not_called()

    @patch('requests.get')
    def test_request_exception(self, mock_get):
        # We need to simulate requests.RequestException
        mock_get.side_effect = requests.RequestException("Connection error")
        scanner = Kustomap("http://example.com?id=1")
        vulns = scanner.scan()
        self.assertEqual(len(vulns), 0)
