import datetime as dt
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
id = input('Meeting id: ') #id of the meeting should be given as input
zoom = wd.Chrome()
zoom.get('https://zoom.us/meetings')
zoom.find_element_by_css_selector('#btnJoinMeeting').click()
elem = zoom.find_element_by_css_selector('#join-confno')
elem.send_keys(id)
elem.send_keys(Keys.RETURN)
sleep(5400) # will automatically exit from the session after 90 mins. If you want you can change this with seconds.
elem.quit()
