from selenium import webdriver
import pytest
import allure
from utilities import logger
import logging
from allure_commons.types import AttachmentType

def pytest_addoption(parser):
	parser.addoption(
		"--browser", action="store", default="firefox")

@pytest.fixture()
def setup(request):
	log = logger.log_util(logging.DEBUG)
	browser = request.config.getoption("--browser")
	base_url = "https://the-internet.herokuapp.com/"
	if browser.lower() == "firefox":
		driver = webdriver.Firefox()
		log.info("Open Firefox browser.")
	elif browser.lower() == "chrome":
		driver = webdriver.Chrome()
		log.info("Open Chrome browser.")

	driver.maximize_window()
	driver.get(base_url)
	request.cls.driver = driver
	before_failed = request.session.testsfailed
	yield
	if request.session.testsfailed != before_failed:
		allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=allure.attachment_type.PNG)
	log.info("Close browser.")
	driver.quit()