from pages.jsalert_page import JsalertPage
import pytest
import time
# import allure

@pytest.mark.usefixtures("setup")
class TestJsalert:

	@pytest.fixture(autouse=True)
	def class_setup(self, setup):
		self.js = JsalertPage(self.driver)

	def test_jsalert(self):
		time.sleep(2)
		self.js.open_page()
		time.sleep(2)
		self.js.open_js_alert()
		time.sleep(2)
		self.js.accept_the_alert()
		time.sleep(2)
		self.js.open_js_confirm()
		time.sleep(2)
		self.js.dismiss_the_alert()
		time.sleep(2)


