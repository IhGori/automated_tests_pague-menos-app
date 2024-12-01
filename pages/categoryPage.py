from pages.basePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import random
import time

class CategoryPage(BasePage):
	
	def to_section(self, locator_type, locator_value):
		self.click(locator_type, locator_value)

	def to_subsection(self, locator_type, locator_value):
		self.click(locator_type, locator_value)

	def get_title(self, locator_type, locator_value):
		title_subsection = self.get_element(locator_type, locator_value)

		return title_subsection

	def select_random_product(self):
		random_product = random.randint(0, 3)

		product = "new UiSelector().className(\"android.widget.ImageView\")"
		self.click(AppiumBy.ANDROID_UIAUTOMATOR, f"{product}.instance({random_product})")

	def return_page(self):
		self.driver.press_keycode(4)
