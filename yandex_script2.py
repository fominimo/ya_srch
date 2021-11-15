from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class YandexTest:

    def __init__(self, target, use_ssl=True):
        self.target = target
        self.protocol = "https" if use_ssl else "http"
        self.driver = webdriver.Firefox()

    def process(self):
        self.driver.get(f"{self.protocol}://{self.target}")
        assert "Яндекс" in self.driver.title
        search = self.driver.find_element('link text', 'Картинки')
        search.click()

        # Проверяем, что перешли
        url = self.driver.current_url
        print(url) # поч не выводит https://yandex.ru/images/ ??????????
        assert url == 'https://yandex.ru/', ('URL не соответствует https://yandex.ru/images/')
        sleep(2)

        # Открываем первую категорию
        first_category = self.driver.find_element('xpath', "(//*[@class = 'PopularRequestList-Item_pos_0'])")
        first_category.click()
        # self.driver.close()


if __name__ == '__main__':
    parser = YandexTest('yandex.ru')
    parser.process()
