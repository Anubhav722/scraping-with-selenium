# common practices of using selenium

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = '/home/sheron/Downloads/chromedriver'
browser = webdriver.Chrome(path)

browser.get('https://google.co.in')

# search bar of google.. search for 'python'

search = browser.find_element_by_name('q')
search.send_keys('python')
search.send_keys(Keys.RETURN)

while True:
	# waiting for elements to load
	browser.implicitly_wait(50)
	# fetching the first result of google using xpath

	try:
		# import ipdb; ipdb.set_trace()
		# //*[@id="rso"]/div[1]/div/div/div/div/h3/a
		search = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/h3/a')
		search.send_keys(Keys.RETURN)
	
		search = browser.find_element_by_xpath('//*[@id="top"]/nav/ul/li[3]/a')
		search.send_keys(Keys.RETURN)
	
		# choosing from the dropdown menu
	
		search = browser.find_element_by_xpath('/html/body/div[1]/ul/li[5]/span/select')
		browser.find_element_by_xpath('/html/body/div[1]/ul/li[5]/span/select/option[text()="2.7"]').click()

		# passing search query 'tutorial' in the search bar
	
		search = browser.find_element_by_xpath('//*[@id="searchbox"]/form/input[1]')
		search.send_keys('tutorial')
		search.send_keys(Keys.RETURN)
	
	
		# fetching all the links from the page
	
		elems = path.find_elements_by_xpath("//a[@href]")
		for elem in elems:
		  print elem.get_attribute("href")
		
		time.sleep(10)
		browser.quit()
	
	except:
		print('Elements do not exist')
