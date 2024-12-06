from pages.basePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import time

class FilterPage(BasePage):
	list_products = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup"
	filter = "//android.widget.TextView[@text='Filtros']"
	button_biggest_price = "//android.widget.TextView[@text='Maior preço']"
	button_show_results = "//android.widget.TextView[@text='Mostrar resultados']"
	first_product_price_on_list = "(//android.view.ViewGroup[@content-desc='btn-detalhes-produto'])[1]/android.view.ViewGroup[4]"
	button_filter_by_brands = "//android.widget.TextView[@text='Marcas']"
	group_total_products = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]"

	def get_list(self, locator_type, locator_value):
		return self.get_elements(locator_type, locator_value)
	
	def open_filter(self):
		self.click(AppiumBy.XPATH, self.filter)
	
	def get_price_first_product(self):
		parent_element = self.get_element(AppiumBy.XPATH, self.first_product_price_on_list)
		child_locator = ".//android.widget.TextView"
		child_element = parent_element.find_element(AppiumBy.XPATH, child_locator)

		return child_element.text
	
	def get_total_products(self):
		parent_element = self.get_element(AppiumBy.XPATH, self.group_total_products)
		child_locator = ".//android.widget.TextView"
		child_element = parent_element.find_element(AppiumBy.XPATH, child_locator)

		return child_element.text

	def filter_by_biggest_price(self):
		self.open_filter()
		self.click(AppiumBy.XPATH, self.button_biggest_price)

	def filter_brand(self):
		self.open_filter()
		self.click(AppiumBy.XPATH, self.button_filter_by_brands)

	def return_page(self):
		self.driver.press_keycode(4)
