from venv import create


def parse_python_code(input_str):
    pattern = r'```python\n(.*?)\n```'
    result = re.search(pattern, input_str, re.DOTALL)
    if result:
        return result.group(1)
    else:
        return "No match found"

def get_repo_filepaths(repo):
    filepaths = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            # Add contents of subfolder
            contents.extend(repo.get_contents(file_content.path))
        else:
            if file_content.path != ".gitignore": # gitignore info just unnecessary tokens
                filepaths.append(file_content.path)
    return filepaths

def get_repo_content_string(repo, filepaths):
    repo_content_string = ""

    for filepath in filepaths:
        repo_content_string += f"FILE PATH:\n{filepath}\nFILE CONTENT:\n"

        file_content = repo.get_contents(filepath).decoded_content
        repo_content_string += f"{file_content}\n\n"

    return repo_content_string

def get_response_content(response):
    return response["choices"][0]["message"]["content"]