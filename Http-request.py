import requests

link = "https://www.google.com.sa/"
f = requests.get(link)
print(f.text)
