# src/github_client.py
from github import Github
import git
import os
from typing import Optional, List

class GitHubClient:
    def __init__(self, token: str):
        self.github = Github(token)
        self.token = token
    
    def get_repository(self, repo_name: str):
        """리포지토리 정보 가져오기"""
        try:
            return self.github.get_repo(repo_name)
        except Exception as e:
            print(f"Repository 접근 오류: {e}")
            return None
    
    def clone_repository(self, repo_url: str, local_path: str):
        """리포지토리 클론"""
        try:
            if os.path.exists(local_path):
                repo = git.Repo(local_path)
                repo.remotes.origin.pull()
                print(f"Repository 업데이트 완료: {local_path}")
            else:
                git.Repo.clone_from(repo_url, local_path)
                print(f"Repository 클론 완료: {local_path}")
            return True
        except Exception as e:
            print(f"클론 오류: {e}")
            return False