import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from pprint import pprint

path = '/home/sheron/Downloads/chromedriver'
browser = webdriver.Chrome(path)
wait = WebDriverWait(browser, 50)
browser.get('https://app.teamwave.com/#/signin?redirect=https:%2F%2Fapp.teamwave.com%2F#%2Fdashboard')

# entering username
# search = browser.find_element_by_xpath('//*[@id="login-email"]')
time.sleep(10)
search = browser.find_element_by_id("login-email").send_keys('info@adhome.com')
# search.send_keys('info@adhome.com')

# entering password
search = browser.find_element_by_xpath('//*[@id="container-login"]/div/div/form/div[2]/input')
# pprint('Please enter your password: ')
search.send_keys(getpass())

# logging in
try:
	pprint("Logging In..")
	search = browser.find_element_by_xpath('//*[@id="container-login"]/div/div/form/div[3]')
	search.click()
	pprint('Logged In')

except:
	pprint('Log In failed')


# wait = WebDriverWait(browser, 50)
# browser.implicitly_wait(5000)


pprint("Fetching links from dashboard ...")
time.sleep(30)

elems = browser.find_elements_by_xpath("//a[@href]")

# elems = browser.find_elements_by_xpath("//a")
count = 0
for elem in elems:
	if elem.text == u'':
		continue
	else:
		count+=1
		pprint(elem.get_attribute('href'))


pprint("Links fetched: %s"%(count))
pprint("The no. of links on the dashboard page: %s"%(len(elems)))
print("\n")

browser.get('https://app.teamwave.com/#/gettingstarted')

pprint("Fetching links from 'Getting Started' ...")
time.sleep(30)

elems = browser.find_elements_by_xpath("//a[@href]")

count = 0

for elem in elems:
	if elem.text == u'':
		continue
	else:
		count+=1
		pprint(elem.get_attribute('href'))

pprint("Links fetched: %s"%(count))
pprint("The no. of links on getting started: %s"%(len(elems)))
print("\n")

browser.get('https://app.teamwave.com/pm/#/projects')

pprint("Fetching links for 'Projects' ...")
time.sleep(30)

count = 0
elems = browser.find_elements_by_xpath("//a[@href]")
for elem in elems:
	if elem.text == u'':
		continue
	else:
		count+=1
		pprint(elem.get_attribute('href'))

pprint("Links fetched: %s"%(count))
pprint("The no. of links for 'Projects': %s"%(len(elems)))
print("\n")

browser.get('https://app.teamwave.com/crm/#/pipeline/default?deal=open&owner=all')

pprint("Fetching links for 'CRM' ...")
time.sleep(30)

count = 0
elems = browser.find_elements_by_xpath("//a[@href]")
for elem in elems:
	if elem.text == u'':
		continue
	else:
		count+=1
		pprint(elem.get_attribute('href'))

pprint("No. of links fetched: %s"%(count))
pprint("The no. of links for 'CRM' %s"%(len(elems)))
print("\n")

browser.get('https://app.teamwave.com/hrm/#/overview/615')

pprint("Fetching links for 'HRM' ...")
time.sleep(30)

count = 0
elems = browser.find_elements_by_xpath("//a[@href]")
for elem in elems:
	if elem.text == u'':
		continue
	else:
		count+=1
		pprint(elem.get_attribute('href'))

pprint("No. of links fetched: %s"%(count))
pprint("The no. of links for 'HRM': %s"%(len(elems)))

browser.quit()