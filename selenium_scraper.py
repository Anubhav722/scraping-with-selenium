from selenium import webdriver
path = '/home/sheron/Downloads/chromedriver'
browser = webdriver.Chrome(executable_path=path)

url = 'https://www.lexisnexis.com/hottopics/lnacademic/?verb=sf&amp;sfi=AC00NBGenSrch'
browser.get(url)

# check here for the frame to switch to
browser.switch_to_frame('mainFrame')

# find elements by id in the respective frame
browser.find_elements_by_id('terms')

# enter text in the search bar
browser.find_element_by_id('terms').clear()

# enter string 'balloon in the search bar
browser.find_element_by_id('terms').send_keys('balloon')

# finding element by xpath
browser.find_element_by_xpath('//*[@id="ddlDateOptions"]')

# entering value into the drop down menu for date.
browser.find_element_by_xpath('//*[@id="ddlDateOptions"]/option[text()="Date is today"]').click()

# click for search button
browser.find_element_by_css_selector('input[type=\"submit\"]').click()
