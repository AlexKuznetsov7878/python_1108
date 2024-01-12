from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import pytest

def test_shop(setup, setup2):
    driver = setup[0]
    wait = setup[1]
    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
    results = driver.find_elements(By.XPATH, "//div[@class='product']")
    for result in results:
        result.find_element(By.XPATH, "div/button").click()
    driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()
    driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
    driver.find_element(By.CLASS_NAME, "promoBtn").click()
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
    result = driver.find_element(By.CLASS_NAME, "promoInfo").text
    assert "Code applied ..!" == result, "TEST FAILED"
    print("TEST PASSED")
