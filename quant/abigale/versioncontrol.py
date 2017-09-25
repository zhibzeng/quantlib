import sys
import os
import shutil
import datetime
from dulwich import porcelain as git


def commit(files, message):
    """
    submit a new git commit if any of the dependencies being changed
    """
    repo = git.Repo(".")
    status = git.status(".")
    unstaged = set(status.unstaged) | set(status.untracked)
    to_submit = set(files) & unstaged
    if to_submit:
        git.add(".", paths=list(to_submit))
        git.commit(".", message)
    return repo.head()
