import requests

url = r"https://google.com/"
headers = {'user-agent': 'my-app/0.0.1'}
params = {"key1": "value1", "key2": "value2"}
payload = {"key1": "value1", "key2": "value2"}

r = requests.get(url=url, headers=headers, timeout=0.1)
p = requests.post(url=url, data=payload)
print(r.status_code)
print(r.text)
