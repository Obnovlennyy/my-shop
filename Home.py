from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollTo(0, 600)")
driver.find_element(By.CSS_SELECTOR,("a .attachment-shop_catalog.size-shop_catalog.wp-post-image:nth-child(1)")).click()
import time
time.sleep(5) #добавлено из-за рекламы
driver.find_element(By.CLASS_NAME,("reviews_tab")).click()
driver.find_element(By.CLASS_NAME,("star-5")).click()
comment = driver.find_element(By.ID,("comment"))
comment.send_keys("Nice book!")
name = driver.find_element(By.ID,("author"))
name.send_keys("QQQ!")
mail = driver.find_element(By.ID,("email"))
mail.send_keys("QQQ@yandex.ru")
driver.find_element(By.ID,("submit")).click()
driver.quit()