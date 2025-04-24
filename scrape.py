from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--user-data-dir=/tmp/unique-profile")

driver = webdriver.Chrome(options=options)
driver.get("https://wd5.myworkday.com/stevens/d/task/3005$3860.htmld")

# time.sleep(60)

ver = input("Input 0, 1, or 2 (0 for Open courses; 1 for Closed courses; 2 for Waitlist courses)\n") # need to make multiple files to obtain ALL classes, scraping the html without it does not get all the results

filename = ""

if (ver == "0"):
    deliv = input("Input delivery mode 0, 1, 2 (0 for in person; 1 for online; 2 for hybrid)\n") # need to select delivery mode here
    if (deliv == "0"):
        filename = "oipcourses.html"
    elif (deliv == "1"):
        filename = "oocourses.html"
    else:
        filename = "ohcourses.html"
elif (ver == "1"):
    filename = "ccourses.html"
else:
    filename = "wlcourses.html"

with open(filename, "w", encoding="utf-8") as f:
    f.write(driver.page_source)


driver.quit()
