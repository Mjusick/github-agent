import os
import requests
from dotenv import load_dotenv
from langchain_core.documents import Document

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def fetch_github(owner, repo, endpoint):
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Fetched data from GitHub: {data}")
        return data
    else:
        print(f"Error fetching data from GitHub: {response.status_code}")
        return []


def load_issues(issues):
    docs = []
    for entry in issues:
        metadata = {
            "author": entry["user"]["login"],
            "comments": entry["comments"],
            "body": entry["body"],
            "labels": entry["labels"],
            "created_at": entry["created_at"],
        }
        data = entry["title"]
        if entry["body"]:
            data += entry["body"]
        doc = Document(page_content=data, metadata=metadata)
        docs.append(doc)
    return docs


def fetch_github_issues(owner, repo):
    data = fetch_github(owner=owner, repo=repo, endpoint="issues")
    issues = load_issues(issues=data)
    return issues
