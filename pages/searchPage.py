from pages.basePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class SearchPage(BasePage):
	search_input = "//android.view.ViewGroup[@content-desc='btn-pesquisa']"
	edit_search_text_input = "//android.widget.EditText[@content-desc='input-pesquisa']"
	error_text = "//android.widget.TextView[@text='Não encontramos nenhum resultado para “abcdefghi”']"
	list_products = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup"

	def open_search(self):
		self.click(AppiumBy.XPATH, self.search_input)
		
	def search_for_product(self, product):
		self.send_keys(AppiumBy.XPATH, self.edit_search_text_input, product)
		self.driver.press_keycode(66)

	def get_message_error(self):
		message_error = self.get_element(AppiumBy.XPATH, self.error_text)
		
		return message_error
	
	def get_list_products(self):
		list_products = self.get_elements(AppiumBy.XPATH, self.list_products)

		return list_products

	def return_page(self):
		self.driver.press_keycode(4)




