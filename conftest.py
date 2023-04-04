# Name : conftest.py
# Author : "Denisov Dmitry"
# Time : 31.03.2023
import pytest, os
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Free Address Book\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--file", action="store", default="groups.xlsx")
    parser.addoption("--n", action="store", default="3")
    parser.addoption("--gen", action="store_true")


@pytest.fixture
def generation(request):
    return request.config.getoption("--gen")
@pytest.fixture
def count_generation(request):
    return request.config.getoption("--n")


@pytest.fixture(scope="session")
def file_path(request):
    return request.config.getoption("--file")
