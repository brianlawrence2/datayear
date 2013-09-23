import requests
import json

query_params = { 'apikey': '151b2c8a7ae74a8791d4ca07ed16aca7',
		 'zip': '37127' }

endpoint = 'http://congress.api.sunlightfoundation.com/legislators/locate'

r = requests.get(endpoint, params=query_params)

parsed = json.loads(r.text)

print json.dumps(parsed, indent=4, sort_keys=True)
