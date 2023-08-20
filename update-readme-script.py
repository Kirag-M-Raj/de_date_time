import requests

# GitHub repository information
username = "Kirag-M-Raj"
repo_name = "de_date_time"
workflow_folder = ".github/workflows"

# Fetch the list of workflow files
response = requests.get(f"https://api.github.com/repos/{username}/{repo_name}/contents/{workflow_folder}")
workflow_files = response.json()

# Fetch the content of each workflow file and generate formatted content
formatted_content = ""
for file_info in workflow_files:
    if file_info["type"] == "file" and file_info["name"].endswith(".yml"):
        file_name = file_info["name"]
        response = requests.get(f"https://raw.githubusercontent.com/{username}/{repo_name}/main/{workflow_folder}/{file_name}")
        workflow_content = response.text
        formatted_content += f"\n## Workflow: {file_name}\n\n```yaml\n{workflow_content}\n```\n"

# Read the current README content
with open("README.md", "r") as readme_file:
    existing_content = readme_file.read()

# Append the generated content to the README
updated_content = existing_content + "\n" + formatted_content
print(updated_content)

# Write the updated content back to the README
with open("README.md", "w") as readme_file:
    readme_file.write(updated_content)
