import requests
import urllib.parse

class Kustomap:
    PAYLOADS = [
        "'",
        '"',
        ";",
        "|",
        "| count",
        "| limit 1",
        " and 1==1",
        " and 1==0",
        " or 1==1",
        " or 1==0",
    ]

    ERROR_STRINGS = [
        "Request is invalid",
        "Syntax error",
        "Semantic error",
        "Kusto request failed",
        "Partial query failure",
    ]

    def __init__(self, url, method="GET", headers=None, data=None):
        self.url = url
        self.method = method.upper()
        self.headers = headers or {}
        self.data = data or {}
        self.vulnerabilities = []

    def scan(self):
        """Scans the URL for KQL injections."""
        if self.method == "GET":
            self._scan_get()
        elif self.method == "POST":
            self._scan_post()
        return self.vulnerabilities

    def _scan_get(self):
        parsed = urllib.parse.urlparse(self.url)
        params = urllib.parse.parse_qs(parsed.query)

        if not params:
            return

        for param, values in params.items():
            for value in values:
                for payload in self.PAYLOADS:
                    # Construct new query string
                    injected_value = value + payload

                    new_params = params.copy()
                    # We only inject one value at a time for simplicity
                    new_params[param] = [injected_value]

                    query_string = urllib.parse.urlencode(new_params, doseq=True)
                    new_url = urllib.parse.urlunparse((
                        parsed.scheme, parsed.netloc, parsed.path,
                        parsed.params, query_string, parsed.fragment
                    ))

                    self._check_injection(new_url, param, payload)

    def _scan_post(self):
        if not self.data:
            return

        for param, value in self.data.items():
             for payload in self.PAYLOADS:
                injected_value = str(value) + payload
                new_data = self.data.copy()
                new_data[param] = injected_value

                self._check_injection(self.url, param, payload, data=new_data)

    def _check_injection(self, url, param, payload, data=None):
        try:
            if self.method == "GET":
                response = requests.get(url, headers=self.headers, timeout=5)
            else:
                response = requests.post(url, headers=self.headers, data=data, timeout=5)

            if self._is_vulnerable(response):
                self.vulnerabilities.append({
                    "param": param,
                    "payload": payload,
                    "url": url,
                    "method": self.method
                })
        except requests.RequestException:
            pass

    def _is_vulnerable(self, response):
        if response.status_code == 500:
            return True
        for error in self.ERROR_STRINGS:
            if error in response.text:
                return True
        return False
