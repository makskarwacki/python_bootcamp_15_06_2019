import json
import urllib.request
import requests

URL = "http://api.nbp.pl/api/exchangerates/tables/B?format=json"

with urllib.request.urlopen(URL) as f:
    xx = f.read()
    results = json.loads(xx)
    print(results)

resp = requests.get(URL)
print(resp.json()[0]['rates'])


