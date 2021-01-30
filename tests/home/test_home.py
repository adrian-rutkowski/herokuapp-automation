from pages.home_page import HomePage
import pytest
import time
# import allure

@pytest.mark.usefixtures("setup")
class TestHomePage:

	@pytest.fixture(autouse=True)
	def class_setup(self, setup):
		self.hp = HomePage(self.driver)

	def test_home(self):
		time.sleep(2)
		assert self.hp.verify_link_ab_present()
		time.sleep(2)
		assert self.hp.verify_link_add_remove_displayed()
		time.sleep(2)


