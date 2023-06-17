#!/usr/bin/python3

from github import Github

# g = Github(login_or_token="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")
# g = Github(auth=auth)

g = Github(base_url="https://api.github.com", login_or_token="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")
username = "dukeofhazardz"
user = g.get_user(username)
repo_name = "alx-higher_level_programming"
repo = g.get_repo(f"{username}/{repo_name}")

if repo:
    print("You are an ALX SE student")
print(user.id)
language = repo.language
print(language)
