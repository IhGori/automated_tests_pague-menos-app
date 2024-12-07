from pages.basePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import random
import time

class SearchPage(BasePage):
	
	edit_search_text_input = "//android.widget.EditText[@content-desc='input-pesquisa']"
	error_text = "//android.widget.TextView[@text='Não encontramos nenhum resultado para “abcdefghi”']"
	list_products = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup"

	first_product_price_on_list = "(//android.view.ViewGroup[@content-desc='btn-detalhes-produto'])[1]/android.view.ViewGroup[4]"
	group_total_products = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]"

	def click_on_element(self, locator_type, locator_value):
		self.click(locator_type, locator_value)

	def search_for_product(self, product):
		self.send_keys(AppiumBy.XPATH, self.edit_search_text_input, product)
		self.driver.press_keycode(66)

	def get_message_error(self):
		message_error = self.get_element(AppiumBy.XPATH, self.error_text)
		
		return message_error
	
	def get_list_products(self):
		list_products = self.get_elements(AppiumBy.XPATH, self.list_products)

		return list_products
	
	def get_list(self, locator_type, locator_value):
		return self.get_elements(locator_type, locator_value)

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

	def return_page(self):
		self.driver.press_keycode(4)




