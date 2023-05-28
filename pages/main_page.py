import time

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Main_page(Base):

    url = 'https://www.wildberries.ru/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #LOCATORS

    menu_burger = "//button[@data-wba-header-name='Catalog']" #Кнопка бургер меню в хедере (каталог)
    catalog_men = "//li[@data-menu-id='566']" #Категория "Мужчины"

    #GETTERS

    def get_menu_burger(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.menu_burger)))

    def get_catalog_men(self):
        return WebDriverWait(self.driver_g, 20).until(EC.element_to_be_clickable((By.XPATH, self.catalog_men)))

    #ACTIONS

    def click_menu_burger(self):
        self.get_menu_burger().click()
        print("Клик на бургер меню")

    def click_catalog_men(self):
        self.get_catalog_men().click()
        print("Клик на категорию")

    #METHODS

    def link_catalog(self): #Данный метод для перехода в любую часть каталога с главной страницы. Нужно лишь подставить необходимый локатор
        self.driver_g.get(self.url)
        self.driver_g.maximize_window()
        self.get_current_url()
        time.sleep(5)
        self.click_menu_burger()
        self.click_catalog_men()
        print("Категория открыта")
