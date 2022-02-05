from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import csv
import requests

# function to check element is present or not
def check_element(xp):
    try:
        if driver.find_element(By.XPATH, xp):
            return True
    except:
        return False

rows = []
# fetching all url data using csv
with open("AmazonScraping.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

les =[]
final_dict = {}
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)
count = 0

print(urls.url_list[:4])
FMT = '%H:%M:%S'
url_count = 0
for row in rows:
    url = (f'https://www.amazon.{row[-1]}/dp/{row[-2]}')
    if url_count == 0:
        start_time = datetime.now().strftime(FMT)
    url_count+=1
    if url_count == 3:
        end_time =  datetime.now().strftime(FMT)
        time_elapsed = datetime.strptime(str(end_time), FMT) - datetime.strptime(str(start_time), FMT)
        print(f'Time taken by 100 URLS parsing:{"#"*10} H:M:S:: {time_elapsed} {"#"*10}\nRe-setting the url counter to zero...')
        url_count = 0
    driver.get(url)
    driver.minimize_window()
    time.sleep(1)
    
    try:
        print('Product URL:\t',url)
        r = requests.get(url)
        print('response code:\t',r.status_code)
        driver.implicitly_wait(10)

        cookies_xpath = '//input[@id="sp-cc-accept"]'
        
        # Cookies Acceptance: checking Cookies accept prompt
        try:
            if driver.find_element(By.XPATH, cookies_xpath).get_attribute('name') == 'accept':
                driver.find_element(By.XPATH, cookies_xpath).click()
        except:
            pass
        
        # Product Title:  checking for title element in the web page and returning title
        try:
            if check_element('//span[@id="productTitle"]'):
                title = (driver.find_element(By.XPATH, '//span[@id="productTitle"]')).text
                print('Product Title:\t',title)
        except:
            print(f'{url}\tcontent not available -- skipping')
            pass

        # price
        if check_element('//div[@id="corePrice_feature_div"]'):
            price = driver.find_element(By.XPATH, '//div[@id="corePrice_feature_div"]').text
        elif driver.find_element(By.XPATH, '(//span[contains(text(),"€")])[1]').text != '':
            price = driver.find_element(By.XPATH, '(//span[contains(text(),"€")])[1]').text
        elif driver.find_element(By.XPATH, '(//span[contains(text(),"€")])[1]').text == '':
            price = driver.find_element(By.XPATH, '(//span[contains(text(),"€")])[2]').text
        print('Price of the Product:\t',price)
        # description
        if check_element('//div[@id="productDescription"]'):
            description = driver.find_element(By.XPATH, '//div[@id="productDescription"]').text
        elif check_element('(//div[@id="detailBullets_feature_div"])[1]'):
            description = driver.find_element(By.XPATH, '(//div[@id="detailBullets_feature_div"])[1]').text
        print('Product Details:\t',description)

        # image url
        if check_element('//div[@id="imgTagWrapperId"]/img'):
            img_url = driver.find_element(By.XPATH, '//div[@id="imgTagWrapperId"]/img').get_attribute('src')
        elif check_element('//div[@id="img-canvas"]/img'):
            img_url = driver.find_element(By.XPATH, '//div[@id="img-canvas"]/img').get_attribute('src')
        print('Product Image URL:\t',img_url)

        count+=1
        print(count)
        final_dict = {
            'index': count,
            'url': url,
            'title':title,
            'img_url': img_url,
            'price':price,
            'description': description,
        }
        les.append(final_dict)

    except Exception as ex:
        print(ex)
        pass
driver.close()

with open('my_json', 'w') as fout:
    fout.write(json.dumps(les, indent=4))

    # printing to check result in console
for d in les:
    print(d,end='\t\n')
