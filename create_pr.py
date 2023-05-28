import openai
from dotenv import load_dotenv
from github import Github, GithubException
import re
import os
from functions import *
import prompts

# load .env variables
load_dotenv()

# Get user inputs
repo_path = input("Enter the repo path. (Example 'Scott-Huston/gpt_dev'):  ")
task_description = input("Enter task description:  ")

# Login and get repo info
g = Github(os.getenv("GH_TOKEN"))
repo = g.get_repo(repo_path)

filepaths = get_repo_filepaths(repo)
repo_content_string = get_repo_content_string(repo, filepaths)

# Authenticate
model = "gpt-4"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create first message
first_message = f"""Here are the contents of a code repository on Github:
{repo_content_string}
Task Description:
{task_description}
{prompts.CLARIFICATION_PROMPT}"""

# Call GPT-4 for clarifying questions
print("Asking what questions the model has. This may take a minute or two")
# TODO wrap api call with try/except to handle errors
response = openai.ChatCompletion.create(
  model=model,
  messages=[
        {"role": "system", "content": prompts.SYSTEM_MESSAGE},
        {"role": "user", "content": first_message}
    ]
)
# TODO add logging of response

question_response = get_response_content(response)
print(question_response)

question_answer = input("Please input your answers to any questions above:  ")

create_pr_message = prompts.CREATE_PR_MESSAGE.format(repo.default_branch, repo.full_name)

# Call GPT-4 for code to generate PR
print("Model is generating the PR. This may take a minute or two")
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": first_message},
        {"role": "assistant", "content": question_responses},
        {"role": "user", "content": f"{response_answer}\n{create_pr_message}"}
    ]
)

create_pr_response = get_response_content(response)

exec(parse_python_code(create_pr_response))
