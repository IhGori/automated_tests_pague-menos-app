from pages.searchPage import SearchPage
from appium.webdriver.common.appiumby import AppiumBy
import time

class TesteSearch:
	search_input = "//android.view.ViewGroup[@content-desc='btn-pesquisa']"
	button_order_by = "//android.widget.TextView[@text='Ordenar por']"
	filter = "//android.widget.TextView[@text='Filtros']"
	option_biggest_price = "//android.widget.TextView[@text='Maior preço']"
	button_filter_by_brands = "//android.widget.TextView[@text='Marcas']"
	
	def test_search_for_a_product_that_does_not_exist(self, driver):
		search_p = SearchPage(driver)

		product = "abcdefghi"
		search_p.click_on_element(AppiumBy.XPATH, self.search_input)
		search_p.search_for_product(product)

		message = search_p.get_message_error()

		assert message.text == f"Não encontramos nenhum resultado para “{product}”", "Erro ao pesquisar produto inexistente"

		search_p.return_page()
		
	def test_search_for_a_product_that_exists(self, driver):
		search_p = SearchPage(driver)

		product = "Sorvete"
		search_p.search_for_product(product)

		items = search_p.get_list_products()
		assert len(items) > 0, f"Erro ao pesquisar por “{product}”"

	def test_search_product_by_highest_price(self, driver):
		search_p = SearchPage(driver)

		price_without_order = search_p.get_price_first_product()

		search_p.click_on_element(AppiumBy.XPATH, self.button_order_by)
		search_p.click_on_element(AppiumBy.XPATH, self.option_biggest_price)

		price_with_order = search_p.get_price_first_product()

		assert price_with_order != price_without_order
