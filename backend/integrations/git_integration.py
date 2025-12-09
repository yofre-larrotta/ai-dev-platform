"""
Git Integration Module
Provides Git operations through GitPython wrapper
"""

from git import Repo, InvalidGitRepositoryError
from pathlib import Path
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class GitManager:
    """Manages Git operations for repositories"""
    
    def __init__(self, repo_path: str = "."):
        """Initialize GitManager with repository path"""
        self.repo_path = Path(repo_path)
        self.repo = None
        self._init_repo()
    
    def _init_repo(self):
        """Initialize or load existing repository"""
        try:
            self.repo = Repo(self.repo_path)
        except InvalidGitRepositoryError:
            logger.info(f"Repository not found at {self.repo_path}")
            self.repo = None
    
    def init_repo(self) -> Dict:
        """Initialize a new Git repository"""
        try:
            self.repo = Repo.init(self.repo_path)
            logger.info(f"Initialized repository at {self.repo_path}")
            return {"status": "success", "message": "Repository initialized"}
        except Exception as e:
            logger.error(f"Failed to initialize repository: {e}")
            return {"status": "error", "message": str(e)}
    
    def add_files(self, files: List[str] = None) -> Dict:
        """Add files to staging area"""
        if not self.repo:
            return {"status": "error", "message": "Repository not initialized"}
        
        try:
            if files:
                self.repo.index.add(files)
            else:
                self.repo.index.add("*")
            
            logger.info(f"Added files to staging area: {files}")
            return {"status": "success", "message": f"Added {len(files) if files else 'all'} files"}
        except Exception as e:
            logger.error(f"Failed to add files: {e}")
            return {"status": "error", "message": str(e)}
    
    def commit(self, message: str) -> Dict:
        """Create a commit with the given message"""
        if not self.repo:
            return {"status": "error", "message": "Repository not initialized"}
        
        try:
            commit = self.repo.index.commit(message)
            logger.info(f"Created commit: {commit.hexsha}")
            return {
                "status": "success",
                "message": f"Committed with SHA: {commit.hexsha}",
                "sha": commit.hexsha[:8]
            }
        except Exception as e:
            logger.error(f"Failed to commit: {e}")
            return {"status": "error", "message": str(e)}
    
    def get_status(self) -> Dict:
        """Get repository status"""
        if not self.repo:
            return {"status": "error", "message": "Repository not initialized"}
        
        try:
            status = {
                "modified": self.repo.index.diff(None),
                "staged": self.repo.index.diff("HEAD"),
                "untracked": self.repo.untracked_files
            }
            return {
                "status": "success",
                "data": {
                    "modified": len(status["modified"]),
                    "staged": len(status["staged"]),
                    "untracked": len(status["untracked"])
                }
            }
        except Exception as e:
            logger.error(f"Failed to get status: {e}")
            return {"status": "error", "message": str(e)}
    
    def get_log(self, max_count: int = 10) -> Dict:
        """Get commit history"""
        if not self.repo:
            return {"status": "error", "message": "Repository not initialized"}
        
        try:
            commits = list(self.repo.iter_commits('HEAD', max_count=max_count))
            log = [
                {
                    "sha": commit.hexsha[:8],
                    "message": commit.message.strip(),
                    "author": commit.author.name,
                    "date": commit.committed_datetime.isoformat()
                }
                for commit in commits
            ]
            return {"status": "success", "data": log}
        except Exception as e:
            logger.error(f"Failed to get log: {e}")
            return {"status": "error", "message": str(e)}
    
    def create_branch(self, branch_name: str) -> Dict:
        """Create a new branch"""
        if not self.repo:
            return {"status": "error", "message": "Repository not initialized"}
        
        try:
            self.repo.create_head(branch_name)
            logger.info(f"Created branch: {branch_name}")
            return {"status": "success", "message": f"Created branch: {branch_name}"}
        except Exception as e:
            logger.error(f"Failed to create branch: {e}")
            return {"status": "error", "message": str(e)}
    
    def list_branches(self) -> Dict:
        """List all branches"""
        if not self.repo:
            return {"status": "error", "message": "Repository not initialized"}
        
        try:
            branches = [head.name for head in self.repo.heads]
            return {"status": "success", "data": branches}
        except Exception as e:
            logger.error(f"Failed to list branches: {e}")
            return {"status": "error", "message": str(e)}
    
    def add_remote(self, name: str, url: str) -> Dict:
        """Add a remote repository"""
        if not self.repo:
            return {"status": "error", "message": "Repository not initialized"}
        
        try:
            self.repo.create_remote(name, url)
            logger.info(f"Added remote: {name} -> {url}")
            return {"status": "success", "message": f"Added remote: {name}"}
        except Exception as e:
            logger.error(f"Failed to add remote: {e}")
            return {"status": "error", "message": str(e)}
    
    def push(self, remote: str = "origin", branch: str = "main") -> Dict:
        """Push changes to remote"""
        if not self.repo:
            return {"status": "error", "message": "Repository not initialized"}
        
        try:
            self.repo.remote(remote).push(branch)
            logger.info(f"Pushed to {remote}/{branch}")
            return {"status": "success", "message": f"Pushed to {remote}/{branch}"}
        except Exception as e:
            logger.error(f"Failed to push: {e}")
            return {"status": "error", "message": str(e)}
    
    def pull(self, remote: str = "origin", branch: str = "main") -> Dict:
        """Pull changes from remote"""
        if not self.repo:
            return {"status": "error", "message": "Repository not initialized"}
        
        try:
            self.repo.remote(remote).pull(branch)
            logger.info(f"Pulled from {remote}/{branch}")
            return {"status": "success", "message": f"Pulled from {remote}/{branch}"}
        except Exception as e:
            logger.error(f"Failed to pull: {e}")
            return {"status": "error", "message": str(e)}