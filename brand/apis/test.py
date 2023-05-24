import gitlab

# Set up GitLab API client
gl = gitlab.Gitlab('https://gitlab.com/', private_token='NsAveRWuj5Yk3TZ7xqZC')

# Get project by ID or path
project = gl.projects.get('95325')

# Monitor issues for "release needed" label
issues = project.issues.list(labels='release needed')
for issue in issues:
    # Create new branch based on master
    branch = project.branches.create({
        'branch': issue.title,
        'ref': 'main'
    })

    # Trigger CI/CD pipeline
    pipeline = project.pi
