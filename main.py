# Selenium main WebDriver
from selenium import webdriver

# Options for browsers (Chrome, Firefox, etc.)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# For waiting until elements appear
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# For sending keyboard keys (like ENTER, TAB)
from selenium.webdriver.common.keys import Keys


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
close = input('enter a key to close')

driver.find_element(By.CLASS_NAME , "L3eUgb" )