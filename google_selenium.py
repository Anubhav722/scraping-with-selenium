import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = '/home/sheron/Downloads/chromedriver'
browser = webdriver.Chrome(path)

browser.get('https://www.google.co.in/')
browser.switch_to_default_content()

search = browser.find_element_by_name('q')
search.send_keys('balloon')
search.send_keys(Keys.RETURN)

time.sleep(10)
browser.quit()
