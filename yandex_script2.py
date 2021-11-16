import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests


class PythonYandexImage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_open_images_in_yandex(self):
        driver = self.driver
        # Переход на яндекс и проверка
        driver.get('https://yandex.ru')
        self.assertIn("Яндекс", driver.title)
        driver.implicitly_wait(2)

        # поиск раздела картинки, нажатие
        search = driver.find_element(By.XPATH, '//a[@data-id="images"]')
        search.click()
        driver.implicitly_wait(5)

        # переход на открывшуюся вкладку
        driver.switch_to.window(driver.window_handles[1])
        sleep(5)

        # Проверка перехода
        url = driver.current_url
        assert url == 'https://yandex.ru/images/?utm_source=main_stripe_big', \
            ('URL не соответствует https://yandex.ru/images/')

        # Открываем первую картинку
        first_image = driver.find_element(
            By.XPATH,
            '//*[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]'
        )
        first_image.click()
        sleep(2)

        # Проверка на открытие
        opened_image = driver.find_element(By.XPATH, '//a[@class="serp-item__link"]')
        opened_image.click()
        sleep(2)
        first_img_url = driver.current_url

        # Нажатие Вперед
        next_button = driver.find_element(By.CSS_SELECTOR, '.MediaViewer-ButtonNext')
        next_button.click()
        sleep(2)
        second_img_url = driver.current_url

        # Проверка, что картинка изменяется
        if first_img_url == second_img_url:
            raise Exception('Картинка не изменилась!')

        # Нажатие Назад
        previous_button = driver.find_element(By.CSS_SELECTOR, '.MediaViewer-ButtonPrev')
        previous_button.click()
        sleep(1)

        # Проверка, что появилась первая картинка
        first_img_url_back = driver.current_url
        if first_img_url != first_img_url_back:
            raise Exception('Не первая картинка!')

        # Берем url картинки
        img_src = driver.find_element(By.XPATH, '//img[@class = "MMImage-Origin"]')
        attrib = img_src.get_attribute('src')

        # Переходим по нему с помощью requests
        resp = requests.get(attrib)

        # Если ответ 200 - считаем, что картинка существует
        if resp.status_code != 200:
            raise Exception('Что не так с источником картинки!')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
