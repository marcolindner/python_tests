from fastapi.testclient import TestClient
from main import app
import re
import json
from bs4 import BeautifulSoup

client = TestClient(app)

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg":"root"}

def test_get_items_headline():
    response = client.get("/items")
    soup = BeautifulSoup(response.text, "html.parser")

    h1_element = soup.find("h1")
    assert h1_element is not None

    h1_text = h1_element.get_text()
    assert h1_text == "Items"

def test_get_items_list():
    response = client.get("/items")
    soup = BeautifulSoup(response.text, "html.parser")

    assert soup.ul.text == "\nItem 1\nItem 2\n"

def test_get_error():
    response = client.get("/error")
    assert response.status_code == 404

def test_get_not_implemeted():
    response = client.get("/notimplemented")
    assert response.status_code == 501



