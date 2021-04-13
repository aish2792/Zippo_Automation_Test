import csv
import pytest
import requests
import json
import jsonpath
from CONSTANTS import *

# BASE_URL = "https://api.zippopotam.us/"

# print(BASE_URL)

# @pytest.mark.country  py.test -m country
# To run test cases in parallel mode - pip install pytest-xdist : py.test -n 5

""" Test countries that have special combinations of zip codes """

def setup_module(module):
    print("*********************** Test Case : test_city_state.py begins ***************************")

def teardown_module(module):
    print("*********************** Test Case : test_city_state.py ends ***************************")

def get_country_state_city(cnty, zipCode):
    """ A function that returns a status code, country, state and city based on the response from the api """

    url = BASE_URL + cnty + "/" + zipCode
    response = requests.get(url)
    statusCode = response.status_code
    json_response = json.loads(response.text)
    country = jsonpath.jsonpath(json_response, "country abbreviation")
    places = jsonpath.jsonpath(json_response, "places")
    countryName = country[0]
    state = places[0][0]['state']
    city = places[0][0]['place name']
    return statusCode, countryName, state, city


def test_status_code():
    """ A function to verify the status code """

    response = requests.get(BASE_URL)
    assert response.status_code == 200, f"url status code expected 200, got {response.status_code}."


@pytest.mark.citystateus
def test_check_us_country_valid_data():
    """ A function to validate city and state in the US, based on the zipcode.  """

    with open(US_TEST_DATA) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for i in data:
            zipCode = i[0] 
            if zipCode == '00210':
                status_code, country_name, state, city = get_country_state_city('us', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
        
            elif zipCode == '00260':
                status_code, country_name, state, city = get_country_state_city('us', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '19144':
                status_code, country_name, state, city = get_country_state_city('us', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '11412':
                status_code, country_name, state, city = get_country_state_city('us', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '99950':
                status_code, country_name, state, city = get_country_state_city('us', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"


@pytest.mark.citystatede
def test_check_de_country_valid_data():
    """ A function to validate city and state in Germany, based on the zipcode.  """

    with open(DE_TEST_DATA) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for i in data:
            zipCode = i[0] 
            if zipCode == '01067':
                status_code, country_name, state, city = get_country_state_city('de', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
        
            elif zipCode == '04571':
                status_code, country_name, state, city = get_country_state_city('de', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '08393':
                status_code, country_name, state, city = get_country_state_city('de', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '10117':
                status_code, country_name, state, city = get_country_state_city('de', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '99998':
                status_code, country_name, state, city = get_country_state_city('de', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"


@pytest.mark.citystatefr
def test_check_fr_country_valid_data():
    """ A function to validate city and state in France, based on the zipcode.  """

    with open(FR_TEST_DATA) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for i in data:
            zipCode = i[0] 
            if zipCode == '01000':
                status_code, country_name, state, city = get_country_state_city('fr', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
        
            elif zipCode == '08300':
                status_code, country_name, state, city = get_country_state_city('fr', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '75008':
                status_code, country_name, state, city = get_country_state_city('fr', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '75001':
                status_code, country_name, state, city = get_country_state_city('fr', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '98799':
                status_code, country_name, state, city = get_country_state_city('fr', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"


@pytest.mark.citystatees
def test_check_es_country_valid_data():
    """ A function to validate city and state in Spain, based on the zipcode.  """

    with open(ES_TEST_DATA) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for i in data:
            zipCode = i[0] 
            if zipCode == '01001':
                status_code, country_name, state, city = get_country_state_city('es', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
        
            elif zipCode == '05001':
                status_code, country_name, state, city = get_country_state_city('es', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '08242':
                status_code, country_name, state, city = get_country_state_city('es', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '09006':
                status_code, country_name, state, city = get_country_state_city('es', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"
            
            elif zipCode == '52080':
                status_code, country_name, state, city = get_country_state_city('es', zipCode)
                assert status_code == 200, f"Status code error: Does not match 200 : {status_code} != 200"
                assert country_name == i[1], f"Country Mismatch : {country_name} != {i[1]}"
                assert state == i[2], f"State Mismatch : {state} != {i[2]}"
                assert city == i[3], f"City Mismatch : {city} != {i[3]}"


                


