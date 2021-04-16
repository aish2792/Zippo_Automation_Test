import pytest
import requests
import json
import jsonpath
from CONSTANTS import *


# @pytest.mark.country  py.test -m country
# To run test cases in parallel mode - pip install pytest-xdist : py.test -n 5

def setup_module():
    print("*********************** Test Case : test_Country_Invalid.py begins ***************************")

def teardown_module():
    print("*********************** Test Case : test_Country_Invalid.py ends ***************************")

def test_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_check_us_country_invalid_data():
    """ Invalid end points """
    url = BASE_URL + "xy/11111"
    response = requests.get(url)
    assert response.status_code == 404, "Status code error: Does not match 404"


def test_check_usa_country_invalid_data():
    """ Invalid end points """

    url = BASE_URL + "usa/11111"
    response = requests.get(url)
    assert response.status_code == 404, "Status code error: Does not match 404"


    