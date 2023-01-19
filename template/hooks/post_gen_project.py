import shutil
import logging
import os
from subprocess import Popen
import logging


# initialize git
git_proc = Popen(["git", "init", str(cwd)])
git_proc.wait()
git_add_proc = Popen(["git", "add", "."])
git_add_proc.wait()
git_commit_proc = Popen(["git", "commit", "-a", "-m", "Initial Cookiecutter commit."])
git_commit_proc.wait()

# versioneer
versioneer_proc = Popen(["versioneer", "install", "--vendor"])
versioneer_proc.wait()
logger.info("Versioneer installed.")

git_add_proc = Popen(["git", "add", "."])
git_add_proc.wait()
git_commit_proc = Popen(["git", "commit", "-a", "-m", "Install versioneer."])
git_commit_proc.wait()

logger.info("Complete.")