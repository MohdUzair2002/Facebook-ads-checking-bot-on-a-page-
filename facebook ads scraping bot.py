from lib2to3.pgen2 import driver
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import csv
data=[]
with open('data1.csv') as file_obj:
  
    reader_obj = csv.reader(file_obj)
      
    for row in reader_obj:
        data.append(str(row[0]))
        
del data[0]      
chrome_options = Options()
S=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=S,options=chrome_options)
i=0
while(i<len(data)):
    browser.get(data[i])
    wait = WebDriverWait(browser, 60)
    browser.maximize_window()
    ads_check=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='button']//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v b1v8xokw py34i1dx'][normalize-space()='See all']")))
    ads_check=browser.find_element(By.XPATH,"//div[@role='button']//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v b1v8xokw py34i1dx'][normalize-space()='See all']")
    browser.execute_script("arguments[0].click();", ads_check)
   
    ads_check1=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='This Page is currently running ads.']")))
    ads_check1=browser.find_element(By.XPATH,"//span[normalize-space()='This Page is currently running ads.']")
    go_to_add_lib=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@aria-label='Go to Ad Library']//div[@class='l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv d1544ag0 tw6a2znq tdjehn4e dwjjeivp']")))
    g0_to_add_lib=browser.find_element(By.XPATH,"//a[@aria-label='Go to Ad Library']//div[@class='l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv d1544ag0 tw6a2znq tdjehn4e dwjjeivp']")
    browser.execute_script("arguments[0].click();", go_to_add_lib)
    time.sleep(30)
    no_of_adds=browser.find_element(By.XPATH,"//div[contains(text(),'~28 results')]")
    print(ads_check1)
    print(no_of_adds)
    # except:
    #     print(f"{data[i]} is not cuurently running the ads")
      
   
    i+=1
