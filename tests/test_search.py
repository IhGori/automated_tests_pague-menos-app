from pages.searchPage import SearchPage
from faker import Faker

class TesteSearch:
	faker = Faker("pt_BR")
	
	def test_search_for_a_product_that_does_not_exist(self, driver):
		search_p = SearchPage(driver)

		product = "abcdefghi"
		search_p.open_search()
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
