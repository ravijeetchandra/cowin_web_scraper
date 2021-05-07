# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  pandas as pd
import winsound
from bs4 import BeautifulSoup
from datetime import datetime
import time

def check_vaccine():
    print("Created by Ravijeet.")
    # Here Chrome  will be used
    driver = webdriver.Chrome()
    now = datetime.now()
     
    # URL of website
    url = "https://www.cowin.gov.in/home"
     
    # Opening the website
    driver.get(url)
     
    # getting the text box by class name
    text_box = driver.find_element_by_id("mat-input-0")
     
    # entering pin code in text box
    text_box.send_keys('313001')
    
    # click on search button
    searchbutton= driver.find_element_by_class_name("pin-search-btn")
    searchbutton.click()
    
    # clicking radio for age 18-44    
    
    # checkBox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "flexRadioDefault2")))   
    # time.sleep(2)
    # checkBox.click()
    # isSelected = driver.find_element_by_id("flexRadioDefault2").is_selected()
    # print(isSelected)
    

    # elements = driver.find_element_by_class_name("center-box")
    elements = WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "center-box")))
    
    time.sleep(2)
        
    #Selenium hands the page source to Beautiful Soup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # covid_centres = soup.find_all("h5", {"class": "center-name-title"})
    
    # flag
    contains_digit = False
    
    booking_status = soup.find_all("div", {"class": 'vaccine-box vaccine-box1 vaccine-padding'})
    for a_booking_status in booking_status:
        # check that slot is available
        result = a_booking_status.text
        if("18+" in result):
            print(result)
            result = result.replace("18+","")
            
            # check for any digit
            for number in result:
                if number.isdigit():
                    contains_digit = True
                    break

        if(contains_digit == True):
            break
                
    if(contains_digit):
        for i in range(0, 10): 
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
        print("Vaccine is available. Check at Cowin website - "+str(now.strftime("%H:%M:%S")))
    else:
        
        print("Vaccine is not available at any centre - "+str(now.strftime("%H:%M:%S")))
            
    driver.close()


check_vaccine()

from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_job(check_vaccine, 'interval', minutes=1)
scheduler.start()









