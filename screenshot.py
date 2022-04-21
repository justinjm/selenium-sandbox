from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime

url = 'https://www.surfline.com/surf-report/crystal-pier/5842041f4e65fad6a7708a73?camId=60c0ffa0daa3c57c71feda47'

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(url)
sleep(1)

out_file = 'screenshot_' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.png'

driver.get_screenshot_as_file(out_file)
driver.quit()
print("end...")