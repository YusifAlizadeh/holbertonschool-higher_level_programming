#!/usr/bin/python3
"""
Displays the GitHub user id using Basic Authentication with a personal
access token.
"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print(None)
