from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.netflix.com/in/browse/genre/34399")

driver.find_element(By.LINK_TEXT, "Uncharted").click()
time.sleep(3)

star = driver.find_element(By.CLASS_NAME, "title-data-info-item-list")
d = driver.find_element(By.CLASS_NAME, "title-info-synopsis")
print(star.text)
print(d.text)

videos = driver.find_element(By.CLASS_NAME, "additional-video-image-wrapper").click()
time.sleep(500)
