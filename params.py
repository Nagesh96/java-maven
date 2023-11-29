import os

git_url = os.environ.get('GIT_URL')
source_branch = os.environ.get('SOURCE_BRANCH')
target_branches = os.environ.get('TARGET_BRANCHES')

print(f"Git URL: {git_url}")
print(f"Source Branch: {source_branch}")
print(f"Target Branches: {target_branches}")
