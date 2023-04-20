from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


# TASK1
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element(By.ID,("menu-item-50")).click()
# import time
# time.sleep(5) #добавлено из-за рекламы
# mail = driver.find_element(By.ID,("username"))
# mail.send_keys("QQQ@yandex.ru")
# password = driver.find_element(By.ID,("password"))
# password.send_keys("StrongPassword322")
# driver.find_element(By.NAME,("login")).click()
# driver.find_element(By.ID,("menu-item-40")).click()
# driver.find_element(By.CSS_SELECTOR,(".post-169 img")).click()
# Old_price = driver.find_element(By.CSS_SELECTOR,(".price del span"))
# Old_price_text = Old_price.text
# New_price = driver.find_element(By.CSS_SELECTOR,(".price ins span"))
# New_price_text = New_price.text
#
# assert Old_price_text =="₹600.00"
# assert New_price_text =="₹450.00"
#
# Book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,(".images"))))
# Book_cover.click()
# Book_cover_close = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR,(".pp_close"))))
# Book_cover_close.click()
# driver.quit()


#TASK2
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element(By.ID,("menu-item-40")).click()
# import time
# time.sleep(5) #добавлено из-за рекламы
# driver.find_element(By.CLASS_NAME,("button.product_type_simple.add_to_cart_button.ajax_add_to_cart")).click()
# # Добавил что было доступно
# time.sleep(10)
# Cart_price = driver.find_element(By.CSS_SELECTOR,(".wpmenucart-contents .amount"))
# Cart_amount = driver.find_element(By.CSS_SELECTOR,(".wpmenucart-contents .cartcontents"))
# #assert Cart_price =="₹350.00"
# #assert Cart_amount =="1 item"
# Cart_price.click()
# time.sleep(10)
# subtotal_price = driver.find_element(By.CSS_SELECTOR,(".cart-subtotal .woocommerce-Price-amount.amount"))
# subtotal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(subtotal_price))
# total_price = driver.find_element(By.CSS_SELECTOR,(".order-total .woocommerce-Price-amount.amount"))
# total = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(subtotal_price))
# #В определенный момент без таймслипов перестал работать код
# driver.quit()

#TASK3
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element(By.ID,("menu-item-40")).click()
# import time
# time.sleep(5) #добавлено из-за рекламы
# driver.find_element(By.CLASS_NAME,("button.product_type_simple.add_to_cart_button.ajax_add_to_cart")).click()
# # Добавил что было доступно
# time.sleep(5)
# driver.find_element(By.CLASS_NAME,("button.product_type_simple.add_to_cart_button.ajax_add_to_cart")).click()
# # Единственная доступная книжка добавил второй раз
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,(".wpmenucart-contents .amount")).click()
# time.sleep(5)
# driver.find_element(By.CLASS_NAME,("remove")).click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,(".woocommerce-message a")).click()
# time.sleep(5)
# Quantity = driver.find_element(By.CLASS_NAME,("input-text.qty.text"))
# Quantity.clear()
# Quantity.send_keys("3")
# driver.find_element(By.NAME, ("update_cart")).click()
# time.sleep(10)
# value = Quantity.get_attribute("value")
# assert value =="3"
# time.sleep(5)
# driver.find_element(By.NAME, ("apply_coupon")).click()
# error_message = driver.find_element(By.CSS_SELECTOR,(".woocommerce-error li"))
# assert error_message =="Please enter a coupon code."
# driver.quit()


#TASK4
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.find_element(By.ID,("menu-item-40")).click()
import time
time.sleep(5) #добавлено из-за рекламы
driver.execute_script("window.scrollTo(0, 300)")
driver.find_element(By.CLASS_NAME,("button.product_type_simple.add_to_cart_button.ajax_add_to_cart")).click()
# # Добавил что было доступно
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,(".wpmenucart-contents .amount")).click()
proceed = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,("checkout-button.button.alt.wc-forward"))))
proceed.click()
F_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,("billing_first_name"))))
F_name.send_keys("Willy")
L_name = driver.find_element(By.ID,("billing_last_name"))
L_name.send_keys("Wonka")
Phone = driver.find_element(By.ID,("billing_phone"))
Phone.send_keys("+998901229181")
Country_selector = driver.find_element(By.ID,("select2-chosen-1"))
Country_selector.click()
Country = driver.find_element(By.ID,("s2id_autogen1_search"))

Country.send_keys("Uzbekistan")
adress = driver.find_element(By.ID,("billing_address_1"))
adress.send_keys("Chilonzor")
city = driver.find_element(By.ID,("billing_city"))
city.send_keys("Tashkent")
state = driver.find_element(By.CSS_SELECTOR,("#billing_state_field #billing_state"))
state.send_keys("Uzbekistan")
postcode = driver.find_element(By.ID,("billing_postcode"))
postcode.send_keys("123456789")
driver.execute_script("window.scrollTo(0, 600)")
time.sleep(5)
driver.find_element(By.ID,("payment_method_cheque")).click()
driver.find_element(By.ID,("place_order")).click()
ThankU = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT,("Thank you. Your order has been received."))))
driver.quit()