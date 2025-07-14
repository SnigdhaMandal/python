import requests

def fetch_github_data(NevroHelios):
    url = f"https://api.github.com/users/{NevroHelios}/repos"
    headers = {
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch data for {NevroHelios}. Status Code:", response.status_code)
        return

    repos = response.json()

    print(f"\n📦 Public Repositories of @{NevroHelios}:\n")
    for repo in repos:
        print(f"🔹 Name        : {repo['name']}")
        print(f"📄 Description: {repo['description']}")
        print(f"💻 Language   : {repo['language']}")
        print(f"⭐ Stars      : {repo['stargazers_count']}")
        print(f"🍴 Forks      : {repo['forks_count']}")
        print(f"🔗 URL        : {repo['html_url']}")
        print("-" * 50)

if __name__ == "__main__":
    github_NevroHelios = input("Enter GitHub NevroHelios: ")
    fetch_github_data(github_NevroHelios)
