#!/usr/bin/python3
from github import Github

g = Github(base_url="https://api.github.com")
check_repo_exists = "alx-system_engineering-devops"

def get_user(username):
    username = g.get_user(username)
    return username

def validate_alx(username):
    repo = g.get_repo(f"{username}/{check_repo_exists}")
    if repo:
        return True

def get_all_repos(username):
    all_repos = []
    username = g.get_user(username)
    repos = username.get_repos()
    for repo in repos:
        repo = str(repo).split('/')[1][:-2]
        all_repos.append(repo)
    return all_repos