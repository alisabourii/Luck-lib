import requests

url = "https://livescore-api.com/api-client/matches/lineups.json?match_id=194137&key=demo_key&secret=demo_secret        "

querystring = {"page":"2"}

headers = {
	"x-rapidapi-key": "8b33fc0c1fmsh1e35e80b5af5be8p1f5100jsn188f58afd56c",
	"x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())