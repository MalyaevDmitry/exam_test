import time

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Product_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #LOCATORS

    name_product = "//h1[text()='Маска Джейсона (Пятница 13-е) Желтая']" #Для проверки товара по имени
    description_product = "//p[@data-link='text{:selectedNomenclature^description}']" #Для проверки описания товара
    up_page = "#mainContainer > button" #Кнопка возврата вверх страницы
    add_cart = "//a[text()='В корзину']" #Кнопка добавления товара в корзину


    #GETTERS

    def get_name_product(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_description_product(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.description_product)))

    def get_up_page(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.up_page)))

    def get_add_cart(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.add_cart)))


    #ACTIONS

    def click_up_page(self):
        self.get_up_page().click()

    def click_add_cart(self):
        self.get_add_cart().click()


    #METHODS

    def check_product(self): #Данный метод для проверки детальной страницы товара и добавления его в корзину
        self.assert_word(self.get_name_product(), 'Маска Джейсона (Пятница 13-е) Желтая')
        self.assert_word(self.get_description_product(),
         'Хоккейная маска Джейсона - убийцы из фильма ужасов слэшера "Пятница13-е". '
         'Подходит для косплея персонажа, Хэллоуина и других костюмированных мероприятий. '
         'Крепится при помощи шлеек на обратной стороне маски. Размер маски: 24,5 * 20 см. Материал маски: пластик.')
        self.driver_g.execute_script("window.scrollTo(0, 1000)") #Данный скролл для того, чтобы отобразился элемент из переменной up_page
        time.sleep(2)
        self.click_up_page()
        time.sleep(1)
        self.driver_g.execute_script("window.scrollTo(0, 1300)") #Данный скролл для проверки кнопки "В корзину"
        time.sleep(1)
        self.click_add_cart()
        time.sleep(1)
        self.click_up_page() #Возврат наверх страницы, чтобы был доступен хедер для отображения
        time.sleep(1)

