from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
contacts = ["FIRST_NAME LAST_NAME"]
msg = "Hey PLACEHOLDER_CONTACT,\n I am an automated message being sent from a python script ;) \n how cool is that!"

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

for contact in contacts:
	text = msg.replace("PLACEHOLDER_CONTACT", contact.split(" ", 1)[0])	
	inp_xpath_search = "//*[@class='_3FRCZ copyable-text selectable-text']"
	#inp_xpath_search = "//*[contains(text(), 'Search or start new chat')]"
	input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
	input_box_search.click()
	time.sleep(2)
	input_box_search.send_keys(contact)
	time.sleep(2)
	selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
	selected_contact.click()
	inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
	input_box = driver.find_element_by_xpath(inp_xpath)
	time.sleep(2)
	input_box.click()
	for line in text.split('\n'):
		#input_box.send_keys(line + Keys.RETURN)
		ActionChains(driver).send_keys(line).perform()
		ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
	ActionChains(driver).send_keys(Keys.RETURN).perform()
	#input_box.send_keys(text + Keys.ENTER)
	time.sleep(2)
driver.quit()
