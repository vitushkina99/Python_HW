from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    input_name = driver.find_element(By.NAME, "custname")
    input_name.send_keys("Ксения")
    button = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    button.click()
    current_url = driver.current_url
    print("Текущий URL:", current_url)
    driver.quit()


test_form_submission()
