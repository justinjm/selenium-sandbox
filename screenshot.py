from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# driver = webdriver.Chrome()
driver.get('https://www.python.org')
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")