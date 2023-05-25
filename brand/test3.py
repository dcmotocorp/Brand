import git

# Set the path to the local repository
repo_path = '/path/to/repository'
repo = git.Repo(repo_path)
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