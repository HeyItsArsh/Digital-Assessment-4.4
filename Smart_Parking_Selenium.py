from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.google.com")

print("Page Title:",driver.title)

if "Google" in driver.title:
    print("Selenium Test: PASS")
else:
    print("Selenium Test: FAIL")

driver.quit()
