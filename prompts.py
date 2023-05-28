

SYSTEM_MESSAGE = "You are a world-class 10X programmer." 
CLARIFICATION_PROMPT = "Do not attempt to complete the task yet. Are there any questions you have about the task before you begin?"
CREATE_PR_MESSAGE = """Ok, now please create a pull request to complete the task using the PyGithub Python library. You should create a new branch, create/modify/delete files as necessary, and then create a pull request.

# Example of creating a branch

source_branch = '{}'
target_branch = 'test'

try:
    # Test to see if branch already exists
    repo.get_branch("test")
except GithubException as e:
    if e.status == 404:
        # If branch does not exist, create it
        sb = repo.get_branch(source_branch)
        repo.create_git_ref(ref='refs/heads/' + target_branch, sha=sb.commit.sha)

# Example of creating a new file
file_content = "This is the file content"
commit_message = "create test file"
repo.create_file(path="test.txt", message=commit_message, content=file_content, branch="test")

# Example of updating a file
contents = repo.get_contents("test.txt", ref="test")
repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="test")

# Example of deleting a file
contents = repo.get_contents("test.txt", ref="test")
repo.delete_file(contents.path, message="remove test", sha=contents.sha, branch="test")

# Example of creating the PR
body = '''
This PR created, updated and deleted a test file
'''
repo.create_pull(title="Test file", body=body, head="test", base=repo.default_branch)


YOUR ENTIRE RESPONSE SHOULD BE EXCLUSIVELY PYTHON CODE. YOUR RESPONSE MUST RUN IN PYTHON AS-IS TO CREATE THE PULL REQUEST.

Your response will be run in a python script after the following code has already been run.

from github import Github, GithubException

# Login and get repo
g = Github(os.getenv("GH_TOKEN"))
repo = g.get_repo({})

"""
