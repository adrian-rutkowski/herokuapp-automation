from pages.iframe_page import IframePage
import pytest
import time
# import allure

@pytest.mark.usefixtures("setup")
class TestIframe:

	@pytest.fixture(autouse=True)
	def class_setup(self, setup):
		self.ifr = IframePage(self.driver)

	def test_iframe(self):
		time.sleep(2)
		self.ifr.open_page()
		time.sleep(2)
		self.ifr.enter_iframe()
		time.sleep(2)
		self.ifr.type_text_in_iframe("Entering some sample text in the frame.")
		time.sleep(2)
		self.ifr.exit_iframe()
		time.sleep(2)
		self.ifr.click_on_elemental()
		time.sleep(2)


