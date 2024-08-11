import requests
from github import Github

# Replace with your GitHub username and the personal access token you created
username = "SyedAbbas6319"
token = "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"

# Authenticate to GitHub
g = Github(token)

# Fetch all public repositories
repos = g.get_user().get_repos()

# Prepare the project section for the README
projects = "\n### 📚 Projects\n\n"
for repo in repos:
    if repo.homepage:
        projects += f"- **[{repo.name}]({repo.html_url})**: {repo.description} - [Live]({repo.homepage})\n"
    else:
        projects += f"- **[{repo.name}]({repo.html_url})**: {repo.description}\n"

# Read the existing README.md file
with open("README.md", "r") as file:
    readme_content = file.read()

# Find the start and end of the projects section
start = readme_content.find("### 📚 Projects")
end = readme_content.find("### 📫 How to reach me")

# Replace the old projects section with the new one
if start != -1 and end != -1:
    new_readme_content = readme_content[:start] + projects + readme_content[end:]
else:
    new_readme_content = readme_content + projects

# Write the updated README.md file
with open("README.md", "w") as file:
    file.write(new_readme_content)

print("README.md updated successfully!")
