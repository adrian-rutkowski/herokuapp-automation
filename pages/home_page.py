from base.basepage import BasePage
from utilities import logger
import logging
import allure

class HomePage(BasePage):

	log = logger.log_util(logging.DEBUG)

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	# Locators
	_ab_testing = "//a[normalize-space()='A/B Testing']"
	_add_remove_elements = "//a[normalize-space()='Add/Remove Elements']"
	_basic_auth = "//a[normalize-space()='Basic Auth']"

	def verify_link_ab_present(self):
		self.log.info("Verify element present.")
		result = self.is_element_present(self._ab_testing)
		return result

	def verify_link_add_remove_displayed(self):
		self.log.info("Verify element displayed.")
		result = self.is_element_displayed(self._add_remove_elements)
		return result

	def verify_link_basic_auth_clickable(self):
		self.log.info("Verify element clickable.")
		result = self.is_element_clickable(self._basic_auth)
		return result