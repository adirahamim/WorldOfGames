from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def test_scores_service(url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    try:
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)
    except NoSuchElementException:
        driver.quit()
        return False
    driver.quit()
    return 1 <= score <= 1000

def main_function():
    #url = "http://localhost:5002"
    url = "http://127.0.0.1:5002"
    if test_scores_service(url):
        return 0
    else:
        return -1

if __name__ == "__main__":
    exit(main_function())
