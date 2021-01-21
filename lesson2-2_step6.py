from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://SunInJuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	# Считать значение для переменной x.
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
    
	# Посчитать математическую функцию от x
	y = calc(x)
	
	# Ввести ответ в текстовое поле.
	result = browser.find_element_by_id("answer")
	result.send_keys(y)
	
	# Отметить checkbox "I'm the robot"
	checkBox = browser.find_element_by_id("robotCheckbox")
	checkBox.click()
	
	# Проскроллить страницу вниз.
	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	assert True
	
	# Выбрать radiobutton "Robots rule!"
	rbRobots = browser.find_element_by_id("robotsRule")
	rbRobots.click()
	
	time.sleep(2)
	
	button.click()	

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

