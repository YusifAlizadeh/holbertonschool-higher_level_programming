#!/usr/bin/python3
"""
Module to fetch posts from JSONPlaceholder and either print titles or save to CSV.
"""

import requests
import csv

JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print their titles.
    """
    response = requests.get(JSONPLACEHOLDER_URL)
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save them to a CSV file.
    Each row contains id, title, and body of a post.
    """
    response = requests.get(JSONPLACEHOLDER_URL)

    if response.status_code == 200:
        posts = response.json()

        # Structure the data into a list of dictionaries
        posts_data = [
            {"id": post.get("id"), "title": post.get("title"), "body": post.get("body")}
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)
