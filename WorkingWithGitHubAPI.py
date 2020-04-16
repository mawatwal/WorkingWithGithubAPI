# Application Programming Interface (API)
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("status code:", r.status_code)
# store api response in a variable
response_dict = r.json()
# process results
print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])
# explore information about the repositories
repo_dicts = response_dict['items']
print("repositories returned:", len(repo_dicts))
# examine the first repository
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

# Summarizing the Top Repositories
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Created:", repo_dict['created_at'])
    print("Updated:", repo_dict['updated_at'])
    print("Description:", repo_dict['description'])
    print("\n")

# Visualizing Repositories using Pygal
names, stars, plot_dicts = [], [], []
for repo_dict in repo_dicts:
    names.append((repo_dict['name']))
    stars.append(repo_dict['stargazers_count'])
my_style = LS(color="#333366", base_style=LCS)
chart = pygal.Bar(Style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most Starred Python Projects on GitHub"
chart.x_labels = names
chart.add("", stars)
chart.render_to_file("python_repos1.svg")

# Refining Pygal Charts
# we make an instance of Pygal's Config class
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 12
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most Starred Python Projects on GitHub"
chart.x_labels = names
chart.add("", stars)
chart.render_to_file("python_repos2.svg")

# Adding Custom Tooltips, clickable links to graph and plotting the data
plot_dict = {'value': repo_dict['stargazers_count'], 'label': repo_dict['description'], 'xlink': repo_dict['html_url']}
plot_dicts.append(plot_dict)
chart.add("", plot_dicts)
chart.render_to_file('python_repos3.svg')