from base.basepage import BasePage
import utilities.logger as log
import logging
import allure

class HoversPage(BasePage):

	log = log.log_util(logging.DEBUG)

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver

	# Locators
	_page = "//a[normalize-space()='Hovers']"
	_image1 = "//div[@class='example']//div[1]//img[1]"
	_user1_link = "//div[@class='example']//div[1]//div[1]//a[1]"

	def open_page(self):
		self.element_click(self._page)
		self.log.info("Open the page.")

	def open_user_profile1(self):
		self.hover_over_and_click(self._image1, self._user1_link)
		self.log.info("Open user profile.")

	def verify_url(self):
		self.get_url()
