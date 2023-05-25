import pygit2
import os 
# Set the path to the GitLab repository
repo_path = '/path/to/repository'

# Open the repository
repo = pygit2.Repository(os.path.dirname(os.path.abspath(__file__)))

# Checkout the master branch
master_branch = repo.branches['master']
repo.checkout(master_branch)

# Iterate over all branches
for branch in repo.branches.local:
    if branch.name != 'master':
        # Checkout the branch
        repo.checkout(branch)

        # Rebase the branch onto the latest changes in master
        rebase_options = pygit2.GitRebaseOptions()
        rebase_options.onto = master_branch.target
        repo.rebase(branch.target, options=rebase_options)

# Checkout the master branch again
repo.checkout(master_branch)

# Print a success message
print("Rebase completed successfully.")
