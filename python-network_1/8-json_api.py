#!/usr/bin/python3
"""
Sends a POST request to search for a user by letter and displays the result.
"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": letter}

    try:
        response = requests.post(url, data=data)
        result = response.json()

        if result:
            print("[{}] {}".format(result.get("id"), result.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
