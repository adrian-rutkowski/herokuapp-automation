from base.basepage import BasePage
import utilities.logger as log
import logging
import allure

class DraganddropPage(BasePage):

	log = log.log_util(logging.DEBUG)

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	# Locators
	_page = "//a[normalize-space()='Drag and Drop']"
	_source = "//div[@id='column-a']"
	_target = "//div[@id='column-b']"

	def open_page(self):
		self.element_click(self._page)
		self.log.info("Open the page.")

	def move_item_a_to_b(self):
		self.drag_and_drop(self._source, self._target)
		self.log.info("Drag A to B.")

