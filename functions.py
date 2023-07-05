#!/usr/bin/python3

import github
from models import storage
from github import Github

g = Github(base_url="https://api.github.com")
check_repo_exists = "alx-system_engineering-devops"

def get_user(username):
    try:
        user = g.get_user(username)
        return user
    except (github.GithubException, github.UnknownObjectException):
        return None

def validate_alx(username):
    try:
        repo = g.get_repo(f"{username}/{check_repo_exists}")
        if repo:
            return True
    except (github.GithubException, github.UnknownObjectException):
        return None

def get_all_repos(username):
    try:
        all_repos = []
        username = g.get_user(username)
        repos = username.get_repos()
        for repo in repos:
            repo_details = {
                "name": repo.name,
                "url": repo.html_url,
                "description": repo.description}
            all_repos.append(repo_details)
        return all_repos
    except (github.GithubException, github.UnknownObjectException):
        return None

def get_bio(user_id):
    bio = storage.get_socials_git(user_id)
    if bio:
        return bio.bio
    return None

def get_title(user_id):
    title = storage.get_socials_git(user_id)
    if title:
        return title.title
    return None

def get_whatido(user_id):
    whatido = storage.get_socials_git(user_id)
    if whatido:
        return whatido.whatido
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

def get_all_user(User):
    all_users = storage.all(User)
    all = [user for user in all_users.values()]
    return all