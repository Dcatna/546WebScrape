from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--user-data-dir=/tmp/unique-profile")

driver = webdriver.Chrome(options=options)
driver.get("https://wd5.myworkday.com/stevens/d/task/3005$3860.htmld")

time.sleep(60)

with open("courses.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

driver.quit()
