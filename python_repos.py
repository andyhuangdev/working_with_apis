import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dic = r.json()
print(f"Total repositories: {response_dic['total_count']}")
print(f"Complete results: {not response_dic['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dic['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dicts = repo_dicts[0]

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dicts['name']}")
    print(f"Owner: {repo_dicts['owner']['login']}")
    print(f"Stars: {repo_dicts['stargazers_count']}")
    print(f"Repository: {repo_dicts['html_url']}")
    print(f"Created: {repo_dicts['created_at']}")
    print(f"Updated: {repo_dicts['updated_at']}")
    print(f"Description: {repo_dicts['description']}")