#!/usr/bin/python3

from github import Github

g = Github(base_url="https://api.github.com")
username = "dukeofhazardz"
user = g.get_user(username)
repo_name = "alx-higher_level_programming"
repo = g.get_repo(f"{username}/{repo_name}")
repos = user.get_repos()
for repo in repos:
    repo = str(repo).split('/')[1]
    repo = repo[:-2]
    print(repo)
print(user.login)


'''if repo:
    print("You are an ALX SE student")
print(user.id)
language = repo.language
print(language)'''
