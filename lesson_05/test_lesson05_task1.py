from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    click_button = driver.find_element(By.LINK_TEXT, "HTML Form")
    click_button.click()
    current_url = driver.current_url
    print("Текущий URL:", current_url)
    driver.back()
    current_url = driver.current_url
    print("Исходный URL:", current_url)

    driver.quit()


test_navigation()
