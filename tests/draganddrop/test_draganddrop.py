from pages.draganddrop_page import DraganddropPage
import pytest
import time
# import allure

@pytest.mark.usefixtures("setup")
class TestHovers:

	@pytest.fixture(autouse=True)
	def class_setup(self, setup):
		self.dnd = DraganddropPage(self.driver)

	def test_dropdown(self):
		time.sleep(2)
		self.dnd.open_page()
		time.sleep(2)
		self.dnd.move_item_a_to_b()
		time.sleep(2)


