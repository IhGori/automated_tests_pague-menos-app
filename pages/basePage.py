from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
	def __init__(self, driver):
		self.driver = driver

	def click(self, locator_type, locator_value):
		WebDriverWait(self.driver, 10).until(
			EC.element_to_be_clickable((locator_type, locator_value))
		).click()

	def send_keys(self, locator_type, locator_value, text):
		WebDriverWait(self.driver, 10).until(
			EC.presence_of_element_located((locator_type, locator_value))
		).send_keys(text)
		
	def get_element(self, locator_type, locator_value):
		element = WebDriverWait(self.driver, 20).until(
			EC.presence_of_element_located((locator_type, locator_value))
		)
		return element

	def get_elements(self, locator_type, locator_value):
		elements = WebDriverWait(self.driver, 20).until(
			EC.presence_of_all_elements_located((locator_type, locator_value))
		)
		return elements
	




