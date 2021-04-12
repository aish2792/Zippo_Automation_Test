import pytest
import requests
import json
import jsonpath

BASE_URL = "https://api.zippopotam.us/"


""" Test Case for the Home Page """

def setup_module(module):
    print("*********************** Test Case - HOME PAGE - Begins ***************************")

def teardown_module(module):
    print("*********************** Test Case - HOME PAGE - Ends ***************************")

def test_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200