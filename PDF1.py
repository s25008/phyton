# This is a sample Python script.
import webbrowser
import requests

date = 20110126
pageUrl = 'www.github.com'
url = "http://archive.org/wayback/available?url="+pageUrl+"&timestamp="+str(date)
response = requests.get(url)
d = response.json()
oldPage = d["archived_snapshots"]["closest"]["url"]

webbrowser.open(oldPage)



