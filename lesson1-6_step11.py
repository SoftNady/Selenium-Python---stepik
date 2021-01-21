from selenium import webdriver
import time 

try:
	link = "http://suninjuly.github.io/registration2.html"
	browser = webdriver.Chrome()
	browser.get(link)

    # Ваш код, который заполняет обязательные поля
	first_name = browser.find_element_by_css_selector("input[required].first")
	first_name.send_keys("Nadejda")
	
	last_name = browser.find_element_by_css_selector("input[required].second")
	last_name.send_keys("Savina")
	
	email = browser.find_element_by_css_selector("input[required].third")
	email.send_keys("soft_nady")
	
	time.sleep(5)

	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector(".btn")
	button.click()

	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(5)

	# находим элемент, содержащий текст
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	# записываем в переменную welcome_text текст из элемента welcome_text_elt
	welcome_text = welcome_text_elt.text

	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

