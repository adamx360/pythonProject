import webbrowser
import requests

pageurl = input("podaj adres strony: ")
date = input("podaj date: ")
url = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date)
response = requests.get(url)
d = response.json()
print(d)
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)
