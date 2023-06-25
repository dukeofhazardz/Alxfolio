#!/usr/bin/python3

from models import storage
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
        all_repos.append(repo.name)
    return all_repos

def get_bio(user_id):

    bio = storage.get_socials_git(user_id)
    if bio:
        return bio.bio
    return None

def get_socials(user_id):
    socials = []
    s = storage.get_socials_git(user_id)
    if s:
        socials.append(s.twitter)
        socials.append(s.instagram)
        socials.append(s.linkedin)
        return socials
    return None

def get_education(user_id):
    education = storage.get_education_git(user_id)
    if education:
        return education
    return None