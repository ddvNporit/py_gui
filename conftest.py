# Name : conftest.py
# Author : "Denisov Dmitry"
# Time : 31.03.2023
import pytest
from fixture.application import Application
@pytest.fixture(scope="session")
def app(request):
    fixture =  Application("C:\\Free Address Book\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture