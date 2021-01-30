from base.basepage import BasePage
import utilities.logger as log
import logging
import allure

class IframePage(BasePage):

	log = log.log_util(logging.DEBUG)

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	# Locators
	_page = "//a[normalize-space()='WYSIWYG Editor']"
	_iframe_id = "mce_0_ifr"
	_text_box = "//body"
	_elemental_link = "//a[normalize-space()='Elemental Selenium']"

	def open_page(self):
		self.element_click(self._page)
		self.log.info("Open the page.")

	def enter_iframe(self):
		self.switch_to_iframe(self._iframe_id)
		self.log.info("Enter iFrame.")

	def type_text_in_iframe(self, text):
		self.clear_field(self._text_box)
		self.send_keys(text, self._text_box)
		self.log.info("Enter text.")

	def exit_iframe(self):
		self.switch_to_default_content()
		self.log.info("Exit the iFrame.")

	def click_on_elemental(self):
		self.element_click(self._elemental_link)
		self.log.info("Click on elemental selenium link to prove that frame changed.")
