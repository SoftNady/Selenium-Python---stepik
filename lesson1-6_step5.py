from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	link2 = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
	link2.click()	
	input1 = browser.find_element_by_name("first_name")
	input1.send_keys("Nadejda")
	input2 = browser.find_element_by_name("last_name")
	input2.send_keys("Savina")
	input3 = browser.find_element_by_class_name("city")
	input3.send_keys("Bishkek")
	input4 = browser.find_element_by_id("country")
	input4.send_keys("Kyrgyzstan")
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(120)
    # закрываем браузер после всех манипуляций
    browser.quit()

