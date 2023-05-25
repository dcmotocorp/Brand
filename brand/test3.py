import git
import os
os.path.abspath(os.getcwd())
# Set the path to the local repository
repo_path = '/'
repo = git.Repo(os.path.abspath(os.getcwd()))
origin = repo.remotes.origin
origin.fetch()
repo.git.checkout('master')
for branch in repo.branches:
    if branch.name == 'master':
        continue
    repo.git.checkout(branch)
    repo.git.rebase('master')
    branch.push(force=True)
repo.git.checkout('master')

print('Rebase completed successfully')