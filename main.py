from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure Chrome to keep window open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, "submit")
# print(button.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

date_elements = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last div ul li time")
dates = [date.text for date in date_elements]

event_elements = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last div ul li a")
events = [event.text for event in event_elements]

events_list = {}
for i in range(len(dates)):
    events_list[i] = {"time": dates[i], "name": events[i]}
# print(events_list)

# close closes a particular tab
driver.close()

# quit closes the entire browser
# driver.quit()
