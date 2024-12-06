from pages.filterPage import FilterPage
from appium.webdriver.common.appiumby import AppiumBy
import time

class TestFilter:
	list_brands = "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[2]"

	def test_whether_filtering_by_highest_price(self, driver):
		filter_p = FilterPage(driver)
		
		price_without_filter = filter_p.get_price_first_product()

		filter_p.filter_by_biggest_price()

		filter_p.return_page()

		price_with_filter = filter_p.get_price_first_product()

		assert price_without_filter != price_with_filter

	def test_filter_by_brands(self, driver):
		filter_p = FilterPage(driver)

		filter_p.filter_brand()

		total_products_without_filter = filter_p.get_total_products()

		time.sleep(10)

		brands = filter_p.get_list(AppiumBy.XPATH, self.list_brands)

		brands[0].click()

		time.sleep(15)

		total_products_with_filter = filter_p.get_total_products()

		assert total_products_without_filter != total_products_with_filter

