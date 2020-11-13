from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import wget

PATH = os.curdir + '\chromedriver'

image = 'FFVAD'
video = 'tWeCl'

def grap(url , className):
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=1920x1080")
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-sh-usage')

	browser = webdriver.Chrome(executable_path = PATH , options = chrome_options)
	browser.get(url)
	time.sleep(2)
	try:
		title = browser.find_element_by_class_name(className)
		image_src = str(title.get_attribute('src')) 
		print(image_src)
		wget.download(image_src)
	except:
		print('Maybe wrong url')
	finally:
		browser.quit();

print('1) Image 2) Video')
choice = int(input())
print('Paste the url')
url = input()

if(choice == 1):
	grap(url , image)
elif (choice == 2):
	grap(url , video)
else :
	print('wrong input')