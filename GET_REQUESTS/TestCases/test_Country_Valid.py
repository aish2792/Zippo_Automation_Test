import pytest
import requests
import json
import jsonpath

BASE_URL = "https://api.zippopotam.us/"



# @pytest.mark.country  py.test -m country
# To run test cases in parallel mode - pip install pytest-xdist : py.test -n 5

""" Test countries """

def setup_module(module):
    print("*********************** Test Case : test_Country_Valid.py begins ***************************")

def teardown_module(module):
    print("*********************** Test Case : test_Country_Valid.py ends ***************************")

def test_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

# US 
def test_check_us_country_valid_data():
    ZIP_CODES = ['00210', '02062', '19144', '11412', '99950']

    for i in ZIP_CODES:
        url = BASE_URL + "us/" + i
        response = requests.get(url)
        # print("Status code is : ", response.status_code)
        json_response = json.loads(response.text)
        country = jsonpath.jsonpath(json_response, "country abbreviation")
        assert country[0] == 'US', "Country Mismatch"
        assert response.status_code == 200, "Status code error: Does not match 200"

# Germany
def test_check_de_country_valid_data():
    ZIP_CODES = ['01067', '04571', '08393', '06279', '99998']

    for i in ZIP_CODES:
        url = BASE_URL + "de/" + i
        response = requests.get(url)
        json_response = json.loads(response.text)
        country = jsonpath.jsonpath(json_response, "country abbreviation")
        assert country[0] == 'DE', "Country Mismatch"
        assert response.status_code == 200, "Status code error: Does not match 200"


# France
def test_check_country_valid_data():
    ZIP_CODES = ['01000', '08300', '75008', '75001', '98799']

    for i in ZIP_CODES:
        url = BASE_URL + "fr/" + i
        response = requests.get(url)
        # print("Status code is : ", response.status_code)
        json_response = json.loads(response.text)
        country = jsonpath.jsonpath(json_response, "country abbreviation")
        assert country[0] == 'FR', "Country Mismatch"
        assert response.status_code == 200, "Status code error: Does not match 200"


# Spain
def test_check_country_valid_data():
    ZIP_CODES = ['01001', '05001', '08242', '09006', '52080']

    for i in ZIP_CODES:
        url = BASE_URL + "es/" + i
        response = requests.get(url)
        # print("Status code is : ", response.status_code)
        json_response = json.loads(response.text)
        country = jsonpath.jsonpath(json_response, "country abbreviation")
        assert country[0] == 'ES', "Country Mismatch"
        assert response.status_code == 200, "Status code error: Does not match 200"



# def test_check_country_invalid_data():
#     for i in ZIP_CODES:
#         url = BASE_URL + "us/" + i
#         response = requests.get(url)
#         print("Response is : ", response.status_code)
#         json_response = json.loads(response.text)
#         country = jsonpath.jsonpath(json_response, "country abbreviation")
#         assert country[0] == 'US', "Country Mismatch"
#         assert response.status_code == 404, "Status code error: Does not match 200"


# def test_check_state_city():
#     url = BASE_URL + "us/19144"
#     response = requests.get(url)
#     json_response = json.loads(response.text)
#     places = jsonpath.jsonpath(json_response, "places")
#     assert places[0][0]['state'] == 'Pennsylvania'
#     assert places[0][0]['place name'] == 'Philadelphia'
#     assert response.status_code == 200, "Status code error: Does not match 200"

    

    
    

    

