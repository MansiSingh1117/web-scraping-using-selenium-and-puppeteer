import time
from selenium.webdriver.support import expected_conditions as EC
import csv
import xlwt
from xlwt import Workbook
import pandas as pd
from csv import writer
from selenium import webdriver
from csv import DictReader
from csv import DictWriter
from selenium.webdriver.support.ui import WebDriverWait



# iterate over each line as a ordered dictionary and print only few column by column name
from urllib3.util import wait
wb=Workbook()
sheet1=wb.add_sheet('Sheet 1',cell_overwrite_ok=False)
i=0
j=0


with open(r'C:\Users\rudra\Downloads\EQUITY_L.csv') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    url = "https://in.finance.yahoo.com"
    driver = webdriver.Chrome(executable_path=r'C:\Users\rudra\OneDrive\Desktop\chromedriver.exe')
    driver.get(url)

    #a = 0

    for row in csv_dict_reader:



            time.sleep(4)
        # action = ActionChains(driver)
            time.sleep(4)

            searchBox = driver.find_element_by_id('yfin-usr-qry')
            time.sleep(4)

            searchBox.send_keys(row['SYMBOL'])
            time.sleep(4)

        # clicking on search
            driver.find_element_by_xpath('//*[@id="search-button"]').click()
            time.sleep(15)

            ticker = driver.find_elements_by_xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1')
            print(ticker[0].text)
            time.sleep(4)
            sheet1.write(i,j, "TICKER:" + ticker[0].text)
            wb.save('xlwt newcsv.xls')
            i=i+1



    read_file=pd.read_excel(r'C:\Users\rudra\PycharmProjects\yahoofinance\venv\xlwt newcsv.xls',sheet_name='Sheet 1')
    read_file.to_csv(r'C:\Users\rudra\PycharmProjects\yahoofinance\venv\xlwt newcsv.csv',index=None)
