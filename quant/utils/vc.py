import sys
import os
from dulwich import porcelain as git


class VersionController:
    # TODO: add dulwich to requirements
    @staticmethod
    def commit(targets, dependencies=None, message=None, repo_dir="."):
        """
        Track the version of target files with git commit id.
        Submit a git commit if any of dependencies being changed.
        
        Parameters
        ----------
        targets: List[str]
            the files to be submitted
        dependencies: List[str] (optional)
            files to be submitted to git
        message: (optional)
            commit message if a commit is nessesary
        """
        commandline = " ".join(sys.argv)
        if not all(os.path.exists(path) for path in targets):
            raise UserWarning("VersionController: targets not exist, quit.")
            return
        head = VersionController._handle_git(dependencies, message, repo_dir)

    @staticmethod
    def _handle_git(dependencies, message, repo_dir):
        """
        submit a new git commit if any of the dependencies being changed

        Parameters
        ----------
        dependencies: List[str] (optional)
            files to be submitted to git
        message: (optional)
            commit message if a commit is nessesary
        repo_dir: str
            path of the repo

        Returns
        -------
        head: str
            Head id of the repo
        """
        repo = git.Repo(repo_dir)
        status = git.status(repo_dir)
        unstaged = set(status.unstaged) | set(status.untracked)
        to_submit = set(dependencies) & unstaged
        if to_submit:
            git.add(repo_dir, paths=list(to_submit))
            git.commit(repo_dir, message)
        return repo.head()

