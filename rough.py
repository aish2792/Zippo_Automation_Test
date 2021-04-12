# import csv

# with open('testdata.csv') as csvfile:
#     data = csv.reader(csvfile, delimiter=',')
#     for i in data:
#         print(i)


import requests
import json
import jsonpath
import csv
import math


parameters = {
    "key" : "0pU2O7yVX0a4pPAYx15l32sb1bf5Yh1q",
    "location" : "00210,US"
}
response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
# print(response.text)
json_response = json.loads(response.text)
# print(json.dumps(json_response, indent=4))

print(json.dumps(json_response["results"][0]["locations"][0], indent=4))
# latLng =jsonpath.jsonpath(json_response, "displayLatLng")
# print(latLng)
latitude = json_response["results"][0]["locations"][0]["latLng"]['lat']

longitude = json_response["results"][0]["locations"][0]["latLng"]['lng']


# print(math.floor(latitude))
# print(math.floor(longitude))




# with open('testdata.csv') as csvfile:
#     data = csv.reader(csvfile, delimiter=',')
#     for i in data:
#         print(i[0])

url = "https://api.zippopotam.us/us/00210"
response1 = requests.get(url)
statusCode = response1.status_code
json_response1 = json.loads(response1.text)
# print(json.dumps(json_response1['places'][0]['longitude'], indent=4))
# print(json.dumps(json_response1['places'][0]['latitude'], indent=4))

lat1 = json_response1['places'][0]['latitude']
lng1 = json_response1['places'][0]['longitude']
# print(math.floor(float(lat1)))
# print(math.floor(float(lng1)))

# places = [[{'place name': 'Portsmouth', 'longitude': '-71.0132', 'state': 'New Hampshire', 'state abbreviation': 'NH', 'latitude': '43.0059'}]]

# print(places[0])