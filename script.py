from github.Issue import Issue
import requests
import os
import json

def count_issues(name, token):
    owner = "TesseractCoding"
    repo = "NeoAlgo"
    author = "name"
    query_url = f"https://api.github.com/search/issues?q=is:issue+repo:{owner}/{repo}+author:{author}+is:open"

    headers = {'Authorization': f'token {token}'}

    r = requests.get(query_url, headers=headers)
    raw=(r.json())
    return raw['total_count']