from pages.hovers_page import HoversPage
import pytest
import time
# import allure

@pytest.mark.usefixtures("setup")
class TestHovers:

	@pytest.fixture(autouse=True)
	def class_setup(self, setup):
		self.hvr = HoversPage(self.driver)

	def test_dropdown(self):
		time.sleep(3)
		self.hvr.open_page()
		time.sleep(3)
		self.hvr.open_user_profile1()
		time.sleep(3)
		# assert self.hvr.verify_url() == "http://the-internet.herokuapp.com/users/1"
		# time.sleep(2)

