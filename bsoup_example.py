import requests

url = "https://quotes.toscrape.com"
page = requests.get(url)
print(page.content)
