#!/usr/bin/python3

from github import Github

g = Github(base_url="https://api.github.com")
username = "dukeofhazardz"
user = g.get_user(username)
#repo_name = "alx-higher_level_programming"
repo_name = "Gitfolio"
repo = g.get_repo(f"{username}/{repo_name}")
repos = user.get_repos()
all_repos = []
for repo in repos:
    repo_details = {
        "name": repo.name,
        "url": repo.html_url,
        "description": repo.description}
    all_repos.append(repo_details)

#print(dir(user))
for repo in repos:
    print([pull for pull in repo.get_pulls()])
"""for v in all_repos:
    print(v)"""
# ["repo_name": foo "details": {"desc": "foo", "url": "bar"}]
# print(user.login)

'''if repo:
    print("You are an ALX SE student")
print(user.id)
language = repo.language
print(language)'''
