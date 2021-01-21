from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	# Нажать на кнопку.
	button = browser.find_element_by_css_selector(".btn")
	button.click()
	
	# Переключиться на новую вкладку
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	
	time.sleep(2)
	
    # Считать значение X.
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	
	# Посчитать функцию от X
	y = calc(x)
	
	# Вписать результат
	result = browser.find_element_by_id("answer")
	result.send_keys(y)	
	
	# Нажать на кнопку Submit.
	button = browser.find_element_by_css_selector(".btn")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

