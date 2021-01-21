from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
	picture = browser.find_element_by_tag_name("img")
		
	# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
	x = picture.get_attribute("valuex")
	print(x)
    
	# Посчитать математическую функцию от x
	y = calc(x)
	
	# Ввести ответ в текстовое поле.
	result = browser.find_element_by_id("answer")
	result.send_keys(y)
	
	# Отметить checkbox "I'm the robot"
	checkBox = browser.find_element_by_id("robotCheckbox")
	checkBox.click()
	
	# Выбрать radiobutton "Robots rule!"
	rbRobots = browser.find_element_by_id("robotsRule")
	rbRobots.click()
	
	time.sleep(2)
	
	# Нажать на кнопку Submit.
	button = browser.find_element_by_css_selector(".btn")
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

