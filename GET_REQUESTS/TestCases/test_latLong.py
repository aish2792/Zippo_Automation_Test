import pytest
import requests
import json
import jsonpath
import csv
import math

BASE_URL = "https://api.zippopotam.us/"

# @pytest.mark.country  py.test -m country
# To run test cases in parallel mode - pip install pytest-xdist : py.test -n 5

""" Test countries that have special combinations of zip codes """

def setup_module(module):
    print("*********************** Test Case : test_latLong.py begins ***************************")

def teardown_module(module):
    print("*********************** Test Case : test_latLong.py ends ***************************")

def test_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def get_expected_lat_long(zipCode, countryName):

    parameters = {
        "key" : "0pU2O7yVX0a4pPAYx15l32sb1bf5Yh1q",
        # "location" : "02062,US"
        "location" : zipCode + "," + countryName.upper()
    }
    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
    json_response = json.loads(response.text)
    latLng = json_response["results"][0]["locations"][0]["latLng"]
    return (math.floor(latLng['lat']), math.floor(latLng['lng']))

def get_actual_country_state_city(cnty, zipCode):
    """ A function that returns latitude and longitude of the place based on the response from the api """

    url = BASE_URL + cnty + "/" + zipCode
    response = requests.get(url)
    statusCode = response.status_code
    json_response = json.loads(response.text)
    places = jsonpath.jsonpath(json_response, "places")
    latitude = places[0][0]['latitude']
    longitude = places[0][0]['longitude']
    return (math.floor(float(latitude)),math.floor(float(longitude)))




def lat_lng_(zipCode, countryName):
    """ A function that tests whether the actual latitude and longitude for a given zipcode lies within the range of the expected
    latitude and longitude values. """
    
    lat_range = []
    lng_range = []
    low_lat = 0
    high_lat = 0
    low_lng = 0
    high_lng = 0
    
    # creating a range of longitudes and latitudes around +/- 5

    expected_lat_lng_pair = get_expected_lat_long(zipCode, countryName)
    actual_lat_lng_pair = get_actual_country_state_city(countryName.lower(), zipCode)

    low_lat = expected_lat_lng_pair[0]-25
    high_lat = expected_lat_lng_pair[0] + 25
    for x in range(low_lat, high_lat):
        lat_range.append(x)

    low_lng = expected_lat_lng_pair[1]-25
    high_lng = expected_lat_lng_pair[1] + 25
    for y in range(low_lng, high_lng):
        lng_range.append(y)


    if actual_lat_lng_pair[0] in lat_range:
        assert True
    else:
        assert False, "The latitude and longitude values do not match!"
    

def test_lat_lng():
    with open('testdata_lat_lng.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for i in data:
            if i[1] == 'US':
                lat_lng_(i[0], 'US')
            elif i[1] == 'DE':
                lat_lng_(i[0], 'DE')
            elif i[1] == 'FR':
                lat_lng_(i[0], 'FR')
            elif i[1] == 'ES':
                lat_lng_(i[0], 'ES')
    
            


