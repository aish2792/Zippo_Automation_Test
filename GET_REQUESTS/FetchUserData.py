import requests
import json
import jsonpath


# API URL
# url = "https://api.zippopotam.us/"
url = "https://api.zippopotam.us/us/02062"

# Send get request
response = requests.get(url)
# print(type(response.content))
# res = response.text
# print(response)

# Display content of the response
# print(response.content)
# print(response.headers)


# Parse to json format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using json path
# country = jsonpath.jsonpath(json_response, "country abbreviation")
# places = jsonpath.jsonpath(json_response, "places")
# print(country[0])
# print(places[0][0]['state'])
# print(places[0][0]['place name'])

# data = {'post code': '19144', 'country': 'United States', 'country abbreviation': 'US', 'places': [{'place name': 'Philadelphia', 'longitude': '-75.1731', 'state': 'Pennsylvania', 'state abbreviation': 'PA', 'latitude': '40.0338'}]}

# print(data['places'][0]['place name'])


