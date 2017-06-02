import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service

service = service.Service('/home/sheron/Desktop/psycho/web-scraper-selenium/chromedriver')
service.start()
capabilities = {'chrome.binary': '/opt/google/chrome'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
driver.quit()
