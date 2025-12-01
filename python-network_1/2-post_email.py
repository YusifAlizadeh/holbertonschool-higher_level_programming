#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter
and displays the decoded body of the response.
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode("utf-8")
        print(body)
