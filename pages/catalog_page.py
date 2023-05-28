import time

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Catalog_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #LOCATORS

    men_kostyumy = "//a[@href='/catalog/muzhchinam/odezhda/kostyumy']" #Категория костюмы
    subcategory_kostyumy = "//button[text()='Категория']" #Подкатегория категории
    karnaval_kostyumy = "//span[text()='Карнавальный костюм']" #Карнавальные костюмы
    color = "//button[text()='Цвет']" #Фильтр по цвету
    value_color = "//span[text()='желтый']" #Выбор цвета
    price = "//button[text()='Цена, ₽']" #Фильтр по цене
    max_price = "//input[@name='endN']" #Поле ввода максимальной цены
    sort_by = "//button[@class='dropdown-filter__btn dropdown-filter__btn--sorter']" #Дропдаун сортировки
    ask_sort_price = "//span[text()='По возрастанию цены']" #Цена по возрастанию
    check_word = "//button[text()='Сбросить все']" #Проверка, что фильтры применились
    pick_product = "//article[@id='c159180965']" #Выбор продукта из списка

    #GETTERS

    def get_men_kostyumy(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.men_kostyumy)))

    def get_subcategory_kostyumy(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.subcategory_kostyumy)))

    def get_karnaval_kostyumy(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.karnaval_kostyumy)))

    def get_color(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.color)))

    def get_value_color(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.value_color)))

    def get_price(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_max_price(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_sort_by(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.sort_by)))

    def get_ask_sort_price(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.ask_sort_price)))

    def get_check_word(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.check_word)))

    def get_pick_product(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.pick_product)))

    #ACTIONS

    def click_men_kostyumy(self):
        self.get_men_kostyumy().click()
        print("Клик на подкатегорию категории")

    def click_subcategory_kostyumy(self):
        self.get_subcategory_kostyumy().click()
        print("Клик на дропдаун категории в фильтрах")

    def click_karnaval_kostyumy(self):
        self.get_karnaval_kostyumy().click()
        print("Клик на нужную категорию в дропдауне ")

    def click_color(self):
        self.get_color().click()
        print("Клик на дропдаун фильтра по цвету")

    def click_value_color(self):
        self.get_value_color().click()
        print("Клик на нужный цвет")

    def click_price(self):
        self.get_price().click()
        print("Клик на фильтр цены")

    def click_max_price(self):
        self.get_max_price().click()
        self.get_max_price().clear()
        self.get_max_price().send_keys('1234')
        print("Клик на поле максимальной цены. Цена установлена")

    def click_sort_by(self):
        self.get_sort_by().click()
        print("Клик на выбор сортировки")

    def click_ask_sort_price(self):
        self.get_ask_sort_price().click()
        print("Клик на нужный вариант сортировки")

    def click_pick_product(self):
        self.get_pick_product().click()
        print("Клик на нужный продукт")


    #METHODS

    def select_category(self): #Данный метод для перехода в любую часть подкатегории с каталога. Нужно лишь подставить необходимый локатор
        self.get_current_url()
        self.click_men_kostyumy()

    def filter(self): #Данный метод для фильтрации товаров. Нужно лишь подставить необходимый локатор
        self.click_subcategory_kostyumy()
        self.click_karnaval_kostyumy()
        time.sleep(1)
        self.click_subcategory_kostyumy()
        time.sleep(1)
        self.click_color()
        time.sleep(1)
        self.click_value_color()
        time.sleep(1)
        self.click_color()
        time.sleep(1)
        self.click_price()
        time.sleep(1)
        self.click_max_price()
        time.sleep(1)
        self.click_price()
        time.sleep(1)
        self.click_sort_by()
        time.sleep(1)
        self.click_ask_sort_price()
        time.sleep(1)
        self.assert_word(self.get_check_word(), 'Сбросить все')

    def pick_products(self): #Данный метод для перехода на страницу товара
        self.click_pick_product()


