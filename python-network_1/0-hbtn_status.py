#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib.

Requirements:
- Use urllib only
- Use a with statement
- Display the body in a specific format
"""

import urllib.request


def main():
    """Fetch the URL and display the formatted response."""
    url = "https://intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    main()
