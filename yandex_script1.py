import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class PythonYandexText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_text_in_yandex(self):
        driver = self.driver
        # Переход на яндекс и проверка
        driver.get('https://yandex.ru')
        self.assertIn("Яндекс", driver.title)

        # ввод 'Тензор' в поиске
        search = driver.find_element('class name', 'input__control')
        search.send_keys("Тензор")
        search.send_keys(Keys.ENTER)
        sleep(2)

        # проверка что в поиске первые 5 результатов включают искомый запрос
        results = self.driver.find_elements('class name', 'serp-item')
        assert [True for i in results[0:5] if 'tensor.ru' in i.find_element('class name', 'link').get_attribute("href")]

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
