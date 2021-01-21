from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	# Дождаться, когда цена дома уменьшится до $100
	price = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	
	# Нажать на кнопку "Book"
	button = browser.find_element_by_id("book")
	button.click()	
	
    # Считать значение X.
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	
	# Посчитать функцию от X
	y = calc(x)
	
	# Вписать результат
	result = browser.find_element_by_id("answer")
	result.send_keys(y)	
	
	# Нажать на кнопку Submit.
	submit = browser.find_element_by_id("solve")
	submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

