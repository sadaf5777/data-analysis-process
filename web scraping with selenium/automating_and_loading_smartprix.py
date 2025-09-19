from selenium import webdriver
from selenium.webdriver.edge.service import Service
s=Service(r'C:/Users/Nadeem Anwar/Downloads/edgedriver_win64/msedgedriver.exe')
from selenium.webdriver.common.by import By

import time


#opening  new window in edge browser

driver=webdriver.Edge(service=s)

#-hitting url 

driver.get('https://www.smartprix.com/mobiles')

#- height of entire page

old_height=driver.execute_script("return document.body.scrollHeight")
print(old_height)

#- loading all items

counter=1
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(old_height)
    print(new_height)
    
    if new_height==old_height:
        break
    old_height = new_height
    counter=counter+1
    print(counter)

#- getting html of entire page

html=driver.page_source

with open ('smartpix.html','w', encoding='utf-8') as f :
    f.write(html)