import datetime


class Base():
    def __init__(self, driver_g):
        self.driver_g = driver_g

    """Получение URL"""

    def get_current_url(self):
        get_url = self.driver_g.current_url
        print(get_url)

    """Проверка по тексту"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Проверка по тексту - ОК")

    """Получение скриншота"""

    def get_screenshot(self):
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver_g.save_screenshot('C:\\Users\\user\\PycharmProjects\\exam_test\\screenshots\\' + name_screenshot)

    """Проверка URL"""

    def assert_url(self, result):
        get_url = self.driver_g.current_url
        assert get_url == result
        print(get_url + "URL - OK")






