from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    driver = webdriver.Chrome()

    return driver


def pytest_addoption(parser):  # this will get the value from cli
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return browser value to the setup method
    return request.config.getoption("--browser")


# it is hook for adding environment info to html report
# def pytest_configure(config):
#     config.metadata['Project Name '] = 'nop commerce'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Prem'
#
#
# #   it is hook for delete /Modify Environment info to html Report
#
# @pytest.mark.optonalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA HOME ", None)
#     metadata.pop("Plugins", None)
