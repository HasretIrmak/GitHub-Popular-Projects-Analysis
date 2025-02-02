import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. GitHub API URL
url = "https://api.github.com/search/repositories?q=stars:>1&sort=stars&order=desc"

# 2. Fetch data from the API
response = requests.get(url)
data = response.json()

# 3. Process the data
repositories = data['items']
repo_data = []

for repo in repositories:
    repo_info = {
        'name': repo['name'],
        'owner': repo['owner']['login'],
        'stars': repo['stargazers_count'],
        'language': repo['language'],
        'url': repo['html_url']
    }
    repo_data.append(repo_info)

# 4. Create a DataFrame
df = pd.DataFrame(repo_data)

# 5. Display the top 5 projects
print("Top 5 Popular Projects:")
print(df.head())

# 6. Count the most starred programming languages
language_counts = df['language'].value_counts()

# 7. Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x=language_counts.index, y=language_counts.values, palette='viridis')
plt.title('Most Popular Programming Languages (by Star Count)')
plt.xlabel('Programming Language')
plt.ylabel('Number of Projects')
plt.xticks(rotation=45)
plt.show()
