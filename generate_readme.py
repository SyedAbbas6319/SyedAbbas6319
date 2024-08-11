import requests

# GitHub API URL to fetch your repositories
url = "https://api.github.com/users/SyedAbbas6319/repos"

# Send a GET request to fetch the repositories
response = requests.get(url)
repos = response.json()

# Open your README file or create a new one
with open("README.md", "w") as file:
    # Write the introduction part
    file.write("# My GitHub Projects\n\n")
    file.write("### 📚 Projects\n\n")

    # Loop through the repositories and write each one to the README
    for repo in repos:
        file.write(f"- [**{repo['name']}**]({repo['html_url']})\n")
        file.write(f"  {repo['description']}\n\n")

print("README.md file updated successfully.")
