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
        search = self.driver.find_element('class name', 'input__control')
        # assert not search or search is None
        search.send_keys("Тензор")
        # assert not self.driver.find_element('class name', 'mini-suggest__overlay_visible')
        search.send_keys(Keys.ENTER)
        # assert not self.driver.find_element('id', 'search-result')
        sleep(2)
        results = self.driver.find_elements('class name', 'serp-item')
        assert [True for i in results[0:5] if 'tensor.ru' in i.find_element('class name', 'link').get_attribute("href")]
        self.driver.close()


if __name__ == '__main__':
    parser = YandexTest('yandex.ru')
    parser.process()
