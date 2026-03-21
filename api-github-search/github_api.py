import requests
param={
    "q":"python",
    "sort":"stars",
    "order":"desc",
    "per_page":5
}
response=requests.get("https://api.github.com/search/repositories",params=param)

data = response.json()
 
repositories = data["items"]
for repo in repositories:
    print(repo["full_name"], "-", repo["stargazers_count"], "stars")