from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def sum(x, y):
  return str(int(x)+int(y))

try:
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

    # Считать значение для переменной num1.
	num1_element = browser.find_element_by_id("num1")
	num1 = num1_element.text
	
	# Считать значение для переменной num2.
	num2_element = browser.find_element_by_id("num2")
	num2 = num2_element.text
	
	# Посчитать сумму найденных чисел
	y = sum(num1, num2)
	
	# Выбрать в выпадающем списке значение равное расчитанной сумме
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(y)
	
	time.sleep(2)
	
	# Нажать на кнопку Submit.
	button = browser.find_element_by_css_selector(".btn")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

