import requests

response = requests.get("https://eaminc.github.io/")
print(response.text)
