import os

# Set your GitHub credentials
GITHUB_USERNAME = 'Halo_mix'
GITHUB_ACCESS_TOKEN = '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'
GITHUB_REPO_NAME = 'O.chiziteremCSC102'

# Get the list of modified files
modified_files = []
for line in os.popen('git status --porcelain').readlines():
    if line.startswith(('M', 'A', 'D')):
        modified_files.append(line.split(maxsplit=1)[1].strip())

# Add modified files to the Git staging area
if modified_files:
    os.system('git add ' + ' '.join(modified_files))

# Delete removed files from the Git repository
for line in os.popen('git status --porcelain').readlines():
    if line.startswith('D'):
        os.system('git rm ' + line.split(maxsplit=1)[1].strip())

# Ask for commit message
commit_message = input('Enter commit message: ')

# Commit the changes
os.system(f'git commit -m "{commit_message}"')

# Push the changes to GitHub
os.system(f'git push https://{GITHUB_USERNAME}:{GITHUB_ACCESS_TOKEN}@github.com/{GITHUB_USERNAME}/{GITHUB_REPO_NAME}.git')
