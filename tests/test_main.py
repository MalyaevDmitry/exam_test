from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.catalog_page import Catalog_page
from pages.product_page import Product_page


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)
    print("Start Test")

    a = Main_page(driver_g)
    a.link_catalog()

    b = Catalog_page(driver_g)
    b.select_category()

    c = Catalog_page(driver_g)
    c.filter()

    d = Catalog_page(driver_g)
    d.pick_products()

    e = Product_page(driver_g)
    e.check_product()

    f = Cart_page(driver_g)
    f.check_cart()

    driver_g.quit()