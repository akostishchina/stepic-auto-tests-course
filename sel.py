import math
def calc(x,y):
	return str(int(x)+int(y))
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1_el = browser.find_element_by_id("num1")
num1 = num1_el.text
num2_el = browser.find_element_by_id("num2")
num2 = num2_el.text
y = calc(num1,num2)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(y)
button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()