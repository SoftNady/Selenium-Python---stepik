from selenium import webdriver
import time 
import os

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
	first_name = browser.find_element_by_name("firstname")
	first_name.send_keys("Nadejda")
	
	last_name = browser.find_element_by_name("lastname")
	last_name.send_keys("Savina")
	
	email = browser.find_element_by_name("email")
	email.send_keys("soft_nady")
	
	# Загрузить файл. 
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt') 
	file_element = browser.find_element_by_id("file")
	file_element.send_keys(file_path)

	# Нажать кнопку "Submit"
	button = browser.find_element_by_css_selector(".btn")
	button.click()	

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()

