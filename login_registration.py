from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element(By.ID,("menu-item-50")).click()
import time
time.sleep(5) #добавлено из-за рекламы
reg_mail = driver.find_element(By.ID,("reg_email"))
reg_mail.send_keys("QQQ@yandex.ru")
reg_password = driver.find_element(By.ID,("reg_password"))
reg_password.send_keys("StrongPassword322")
driver.find_element(By.NAME,("register")).click()
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element(By.ID,("menu-item-50")).click()
import time
time.sleep(5) #добавлено из-за рекламы
mail = driver.find_element(By.ID,("username"))
mail.send_keys("QQQ@yandex.ru")
password = driver.find_element(By.ID,("password"))
password.send_keys("StrongPassword322")
driver.find_element(By.NAME,("login")).click()
driver.find_element(By.LINK_TEXT,("Logout"))
driver.quit()