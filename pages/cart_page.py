import time

from selenium.webdriver import Keys, ActionChains

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #LOCATORS

    open_cart = "//a[text()='            Корзина        ']" #Открытие корзины
    count_products = "//button[@class='count__plus plus']" #Кол-во товара в большую сторону
    input_count_products = "//input[@type='number']" #Поле ввода кол-ва товара
    delivery_1 = "//div[@class='basket-delivery__choose-address j-btn-choose-address']" #Выбор доставки
    input_adress = "//ymaps/input[@class='ymaps-2-1-79-searchbox-input__input'][@autocomplete='off']" #Поле ввода адреса
    value_adress = "//span[@class='address-item__name-text']/span[text()='г. Москва, м Жулебино, ул. Генерала Кузнецова, 14 корп. 1']" #Выбор пункта выдачи
    pick_adress = "//button[@class='details-self__btn btn-main']" #Подтверждение выбор пункта выдачи
    order = "//button[@class='b-btn-do-order btn-main j-btn-confirm-order']" #Кнопка заказать



    #GETTERS

    def get_open_cart(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.open_cart)))

    def get_count_products(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.count_products)))

    def get_input_count_products(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.input_count_products)))

    def get_delivery_1(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.delivery_1)))

    def get_input_adress(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.input_adress)))

    def get_value_adress(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.value_adress)))

    def get_pick_adress(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.pick_adress)))

    def get_order(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.order)))


    #ACTIONS

    def click_open_cart(self):
        self.get_open_cart().click()

    def click_count_products(self):
        action = ActionChains(self.driver_g)
        action.double_click(self.get_count_products()).perform()

    def click_input_count_products(self):
        self.get_input_count_products().click()
        self.get_input_count_products().send_keys(Keys.ARROW_RIGHT)
        self.get_input_count_products().send_keys(Keys.BACKSPACE)
        self.get_input_count_products().send_keys('2')
        self.get_input_count_products().send_keys(Keys.RETURN)

    def click_delivery_1(self):
        self.get_delivery_1().click()

    def click_input_adress(self):
        self.get_input_adress().click()
        self.get_input_adress().send_keys('Москва')
        self.get_input_adress().send_keys(Keys.RETURN)

    def click_value_adress(self):
        self.get_value_adress().click()

    def click_pick_adress(self):
        self.get_pick_adress().click()

    def click_order(self):
        self.get_order().click()



    #METHODS

    def check_cart(self): #Данный метод для совершения действий в корзине. Выбор доставки и заказа.
        self.click_open_cart()
        self.click_count_products()
        time.sleep(2)
        self.click_input_count_products()
        time.sleep(2)
        self.click_delivery_1()
        time.sleep(2)
        self.click_input_adress()
        self.click_value_adress()
        self.click_pick_adress()
        time.sleep(2)
        self.click_order()


