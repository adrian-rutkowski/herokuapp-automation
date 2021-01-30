from base.basepage import BasePage
import utilities.logger as log
import logging
import allure


class DropdownPage(BasePage):
	log = log.log_util(logging.DEBUG)

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	# Locators
	_page = "//a[contains(text(),'Dropdown')]"
	_dropdown = "//select[@id='dropdown']"

	def open_page(self):
		self.element_click(self._page)
		self.log.info("Open the page.")

	def choose_dropdown_value(self, text=""):
		self.dropdown_value_select_by_text(self._dropdown, text)
		self.log.info("Select dropdown value: " + text)
