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
    message = message or "committed @ {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    if isinstance(message, str):
        message = message.encode("utf-8")
    if to_submit:
        git.add(".", paths=list(to_submit))
        git.commit(".", message)
    commit_id = repo.head()
    if not isinstance(commit_id, str):
        commit_id = commit_id.decode("utf-8")
    return commit_id
