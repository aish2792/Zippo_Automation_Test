import pytest
import requests
import json
import jsonpath
from CONSTANTS import *


""" Base Test Cases """

def setup_module(module):
    print("*********************** Test Case - HOME PAGE - Begins ***************************")

def teardown_module(module):
    print("*********************** Test Case - HOME PAGE - Ends ***************************")

def test_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

# test response headers
@pytest.mark.responseheaders
def test_response_header():
    response = requests.head(BASE_URL)
    print(response.headers)
    assert response.headers["Content-Type"] == 'text/html; charset=UTF-8', f'Content-Type is not html'
