import pytest
import requests
import json
import jsonpath
import csv
import math
from CONSTANTS import *

# @pytest.mark.country  py.test -m country
# To run test cases in parallel mode - pip install pytest-xdist : py.test -n 5

""" Test countries that have special combinations of zip codes """

def setup_module():
    print("*********************** Test Case : test_lat_lng.py begins ***************************")

def teardown_module():
    print("*********************** Test Case : test_lat_lng.py ends ***************************")

def test_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


def get_expected_lat_long(zipCode, countryName):
    """ A function that returns latitude and longitude pair using zipcode - mapquest api"""

    parameters = {
        "key" : "0pU2O7yVX0a4pPAYx15l32sb1bf5Yh1q",
        "location" : zipCode + "," + countryName.upper()
    }
    response = requests.get(MAPQUEST_URL, params=parameters)
    json_response = json.loads(response.text)
    latLng = json_response["results"][0]["locations"][0]["latLng"]
    return (math.floor(latLng['lat']), math.floor(latLng['lng']))


def get_actual_country_state_city(cnty, zipCode):
    """ A function that returns latitude and longitude of the place based on the response from the api """

    url = BASE_URL + cnty + "/" + zipCode
    response = requests.get(url)
    statusCode = response.status_code
    if statusCode == 200:
        json_response = json.loads(response.text)
        places = jsonpath.jsonpath(json_response, "places")
        latitude = places[0][0]['latitude']
        longitude = places[0][0]['longitude']
        return (math.floor(float(latitude)),math.floor(float(longitude)))
    else:
        return statusCode


def lat_lng_(zipCode, countryName):
    """ A function that tests whether the actual latitude and longitude for a given zipcode lies within the range of the expected
    latitude and longitude values. """

    TOLERANCE = 100

    expected_lat, expected_lng = get_expected_lat_long(zipCode, countryName)
    actual_lat, actual_lng = get_actual_country_state_city(countryName.lower(), zipCode)

    assert actual_lat in range(expected_lat - TOLERANCE, expected_lat + TOLERANCE), f"The latitude values do not match! : {expected_lat} != {actual_lat}"
    assert actual_lng in range(expected_lng - TOLERANCE, expected_lng + TOLERANCE), f"The longitude values do not match! : {expected_lng} != {actual_lng}"

    
# happy scenario
@pytest.mark.latlng
def test_lat_lng():
    with open(TEST_DATA_LAT_LNG) as csvfile:
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
            else:
                print("The validation is for US, DE, FR and ES countries! Please check the country.")


# negative scenario
@pytest.mark.latlng
def test_lat_lng_invalid():
    with open(TEST_DATA_INVALID) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for i in data:
            if i[1] == 'US':
                statusCode = get_actual_country_state_city("US", i[0])
                assert statusCode == 404

            elif i[1] == 'DE':
                statusCode = get_actual_country_state_city("US", i[0])
                assert statusCode == 404

            elif i[1] == 'FR':
                statusCode = get_actual_country_state_city("US", i[0])
                assert statusCode == 404

            elif i[1] == 'ES':
                statusCode = get_actual_country_state_city("US", i[0])
                assert statusCode == 404

            else:
                print("The validation is for US, DE, FR and ES countries! Please check the country.")

    
            


