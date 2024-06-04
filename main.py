import requests
import json
Response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") 
jsonString = Response.text
result = json.loads(jsonString)


print(result["bpi"]["USD"]["rate"])
