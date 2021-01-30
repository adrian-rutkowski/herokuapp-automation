from base.basepage import BasePage
import utilities.logger as log
import logging
import allure

class JsalertPage(BasePage):

	log = log.log_util(logging.DEBUG)

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	# Locators
	_page = "//a[normalize-space()='JavaScript Alerts']"
	_js_alert = "//button[normalize-space()='Click for JS Alert']"
	_js_confirm = "//button[normalize-space()='Click for JS Confirm']"

	def open_page(self):
		self.element_click(self._page)
		self.log.info("Open the page.")

	def open_js_alert(self):
		self.element_click(self._js_alert)
		self.log.info("Open JS alert.")

	def accept_the_alert(self):
		self.accept_js_alert()
		self.log.info("Click OK on JS alert.")

	def open_js_confirm(self):
		self.element_click(self._js_confirm)
		self.log.info("Open JS confirm.")

	def dismiss_the_alert(self):
		self.dismiss_js_alert()
		self.log.info("Click CANCEL on  JS alert.")


