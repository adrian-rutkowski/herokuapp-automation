from pages.dropdown_page import DropdownPage
import pytest
import time
# import allure

@pytest.mark.usefixtures("setup")
class TestDropdown:

	@pytest.fixture(autouse=True)
	def class_setup(self, setup):
		self.dp = DropdownPage(self.driver)

	def test_dropdown(self):
		time.sleep(3)
		self.dp.open_page()
		time.sleep(3)
		self.dp.choose_dropdown_value(text="Option 2")
		time.sleep(3)
