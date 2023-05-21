from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

download_directory = "/app/csv/"

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
 
browser = webdriver.Chrome(options=chrome_options)

browser.get('https://www.tradingview.com/#signin')
username = 'xx'
password = 'yy'


time.sleep(2)

#Email click
wait = WebDriverWait(browser, 10)
wait.until(EC.visibility_of_element_located((By.NAME, 'Email'))).click()

print("login")
browser.get_screenshot_as_file('/app/screenshots/0_login.png') 

# compile login form
username_input = browser.find_element(By.NAME, 'id_username')
username_input.send_keys(username)

password_input = browser.find_element(By.NAME, 'id_password')
password_input.send_keys(password)

password_input.send_keys(Keys.RETURN)
time.sleep(2)

# get symbol page
ticker_symbol = 'CNLIVRR'
url_ticker = f'https://www.tradingview.com/chart/BlxZCwOJ/?symbol={ticker_symbol}'
browser.get(url_ticker)
time.sleep(1)
print("get chart")
browser.get_screenshot_as_file('/app/screenshots/1_getpage.png') 

# load menu for save and load
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.apply-common-tooltip[data-name="save-load-menu"]'))).click()
time.sleep(1)
print("open menu")
browser.get_screenshot_as_file('/app/screenshots/2_openmenu.png') 

wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Export chart data…')]"))).click()
time.sleep(1)
print("open export popup")
browser.get_screenshot_as_file('/app/screenshots/3_exportpopup.png') 

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#overlap-manager-root button[name="submit"]'))).click()
time.sleep(1)
print("export button click")
browser.get_screenshot_as_file('/app/screenshots/4_exportbutton.png') 

browser.quit()
