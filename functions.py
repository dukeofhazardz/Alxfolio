#!/usr/bin/python3

import github
import json
from models import storage
from github import Github
from redis import Redis
from datetime import timedelta

redis_client = Redis(host='localhost', port=6379, db=0)

def get_user(username):
    user = redis_client.get(f"{username}")
    if user is None:
        try:
            g = Github(base_url="https://api.github.com")
            user_dict = vars(g.get_user(username))
            user = {key : value for key, value in user_dict.items() if key.startswith('_rawData')}
            user = user['_rawData']
            redis_client.set(f"{username}", json.dumps(user))
            redis_client.expire(f"{username}", timedelta(hours=24))
        except (github.GithubException, github.UnknownObjectException):
            return None
    else:
        user = json.loads(user)
    return user

def validate_alx(username):
    repo = redis_client.get(f"{username}"+"_repo")
    if repo is None:
        try:
            g = Github(base_url="https://api.github.com")
            check_repo_exists = "alx-system_engineering-devops"
            repo = g.get_repo(f"{username}/{check_repo_exists}")
            if repo:
                redis_client.set(f"{username}"+"_repo", 1)
                redis_client.expire(f"{username}"+"_repo", timedelta(hours=24))
        except (github.GithubException, github.UnknownObjectException):
            return None
    return True

def get_all_repos(username):
    all_repos = redis_client.get(f"{username}"+"_all_repos")
    if all_repos is None:
        try:
            g = Github(base_url="https://api.github.com")
            all_repos = []
            user = g.get_user(username)
            repos = user.get_repos()
            for repo in repos:
                repo_details = {
                    "name": repo.name,
                    "url": repo.html_url,
                    "description": repo.description}
                all_repos.append(repo_details)
            redis_client.set(f"{username}"+"_all_repos", json.dumps(all_repos))
            redis_client.expire(f"{username}"+"_all_repos", timedelta(hours=24))
        except (github.GithubException, github.UnknownObjectException):
            return None
    else:
        all_repos = json.loads(all_repos)
    return all_repos

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