from pages.categoryPage import CategoryPage
from appium.webdriver.common.appiumby import AppiumBy

class TestCategory:
	TITLE_SUBSECTION_OUR_BRANDS = "//android.widget.TextView[@text='Selecione uma de nossas marcas']"
	TITLE_SUBSECTION_FITNESS_AND_NUTRITION = "//android.widget.TextView[@text='Selecione uma Subcategoria']"
	SUBSECTION_FITNESS_AND_NUTRITION = "//android.view.ViewGroup[@content-desc='btn-categoria-6']/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[1]"
	TITLE_PAGE_PRODUCT = "//android.widget.TextView[@text='Produto']"
	CATEGORY_SECTION = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View/android.view.View[2]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[1]"
	HOME_SECTION = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View/android.view.View[1]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[2]"

	def test_category_navigation_on_subsections(self, driver):
		category_p = CategoryPage(driver)
		category_p.to_section(AppiumBy.XPATH, self.CATEGORY_SECTION)

		title_page_subsection_our_brands = category_p.get_title(AppiumBy.XPATH, self.TITLE_SUBSECTION_OUR_BRANDS)
		assert title_page_subsection_our_brands.text == 'Selecione uma de nossas marcas', (
			"Não encontrou o título da subseção de categorias 'Nossas marcas'"
		)

		category_p.to_subsection(AppiumBy.XPATH, self.SUBSECTION_FITNESS_AND_NUTRITION)
		title_page_subsection_fitness_and_nutrition = category_p.get_title(AppiumBy.XPATH, self.TITLE_SUBSECTION_FITNESS_AND_NUTRITION)
		assert title_page_subsection_fitness_and_nutrition.text == 'Selecione uma Subcategoria', (
			"Não encontrou o título da subseção de categorias 'Fitness e Nutrição'"
		)

	def test_can_select_a_product(self, driver):
		category_p = CategoryPage(driver)
		category_p.select_random_product()

		title_page_product = category_p.get_title(AppiumBy.XPATH, self.TITLE_PAGE_PRODUCT)
		assert title_page_product.text == 'Produto', "Não acessou a página do produto selecionado"
		
		category_p.return_page()

