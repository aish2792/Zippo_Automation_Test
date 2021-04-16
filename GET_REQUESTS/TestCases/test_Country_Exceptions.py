import pytest
import requests
import json
import jsonpath
from CONSTANTS import *

# @pytest.mark.country  py.test -m country
# To run test cases in parallel mode - pip install pytest-xdist : py.test -n 5

""" Test countries that have special combinations of zip codes """

def setup_module():
    print("*********************** Test Case : test_country_exceptions.py begins ***************************")

def teardown_module():
    print("*********************** Test Case : test_country_exceptions.py ends ***************************")

def test_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


# Canada
def test_check_country_ca_exceptions():
    ZIP_CODES = ['A0A', 'N9V', 'K1A', 'T9S', 'Y1A']
    for i in ZIP_CODES:
        url = BASE_URL + "ca/" + i
        response = requests.get(url)
        json_response = json.loads(response.text)
        country = jsonpath.jsonpath(json_response, "country abbreviation")
        assert country[0] == 'CA', "Country Mismatch"
        assert response.status_code == 200, "Status code error: Does not match 200"


# Argentina
def test_check_country_ar_exceptions():
    ZIP_CODES = ['1601', '1865', '8000', '6450', '9431']
    for i in ZIP_CODES:
        url = BASE_URL + "ar/" + i
        response = requests.get(url)
        json_response = json.loads(response.text)
        country = jsonpath.jsonpath(json_response, "country abbreviation")
        assert country[0] == 'AR', "Country Mismatch"
        assert response.status_code == 200, "Status code error: Does not match 200"


# Brazil
def test_check_country_br_exceptions():
    ZIP_CODES = ['01000-000', '58000-000', '69000-000', '79000-000', '99990-000']
    for i in ZIP_CODES:
        url = BASE_URL + "br/" + i
        response = requests.get(url)
        json_response = json.loads(response.text)
        country = jsonpath.jsonpath(json_response, "country abbreviation")
        assert country[0] == 'BR', "Country Mismatch"
        assert response.status_code == 200, "Status code error: Does not match 200"

