import pygit2
import os 
# Set the path to the GitLab repository
repo_path = '/path/to/repository'

# Open the repository
repo = pygit2.Repository(os.path.dirname(os.path.abspath(__file__)))

# Get the master branch
master_branch = repo.branches['master']

# Iterate over all branches
for branch_name in repo.branches.remote:
    # Skip the master branch
    if branch_name == 'master':
        continue

    # Get the branch reference
    branch_ref = repo.branches[branch_name]

    # Create a temporary branch for the rebase
    temp_branch_name = f'temp/{branch_name}'
    temp_branch_ref = repo.create_branch(temp_branch_name, branch_ref.target)
    temp_branch_ref.upstream = master_branch.target

    # Checkout the temporary branch
    repo.checkout(temp_branch_name)

    # Perform the rebase manually
    repo.merge(temp_branch_ref.target)

    # Update the branch reference with the rebased commits
    branch_ref.set_target(temp_branch_ref.target)

    # Push the rebased branch to the GitLab repository
    remote_name = 'origin'
    remote = repo.remotes[remote_name]
    remote.push([f'{branch_name}:{branch_name}'])

    # Delete the temporary branch
    repo.branches.delete(temp_branch_name)
