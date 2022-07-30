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
k=1
l=2
m=3
n=4
with open(r'C:xxxxxxxx\ms.csv') as read_obj:#path of the downloaded equity_l file from nse
    csv_dict_reader = DictReader(read_obj)
    url = "https://in.finance.yahoo.com"
    driver = webdriver.Chrome(executable_path=r'C:\xxxxxxxx\chromedriver.exe')
    driver.get(url)
    #a = 0

    for row in csv_dict_reader:
        time.sleep(5)
        # action = ActionChains(driver)
        time.sleep(5)

        searchBox = driver.find_element_by_id('yfin-usr-qry')
        time.sleep(5)

        searchBox.send_keys(row['SYMBOL'])
        time.sleep(5)

        # clicking on search
        driver.find_element_by_xpath('//*[@id="search-button"]').click()
        time.sleep(20)


        EPS = driver.find_elements_by_xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[4]/td[2]/span')
        time.sleep(5)
        print("EPS(TTM):"+EPS[0].text)
        sheet1.write(i,j,"EPS(TTM):"+EPS[0].text)



        target_est=driver.find_elements_by_xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[8]/td[2]/span')
        time.sleep(5)
        print("1year target est:"+target_est[0].text)
        sheet1.write(i,k, "1y target est:" + target_est[0].text)


        PE= driver.find_elements_by_xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[2]/span')
        time.sleep(5)
        print("PE ratio(TTM):" +PE[0].text)
        sheet1.write(i,l, "PE ratio(TTM)" + PE[0].text)


        OP= driver.find_elements_by_xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]/span')
        time.sleep(5)
        print("OPEN:" + OP[0].text)

        sheet1.write(i,m, "OPEN:" + OP[0].text)


        FD= driver.find_elements_by_xpath('// *[ @ id = "quote-summary"] / div[2] / table / tbody / tr[6] / td[2]')
        time.sleep(5)
        print("FORWARD DIVIDEND:" +FD[0].text)

        sheet1.write(i,n, "FD:" + FD[0].text)


        wb.save('xlwt summary.xls')


        i=i+1
        #filepath and name.xls
    read_file=pd.read_excel(r'C:\xxxxxxx\venv\xlwt summary.xls',sheet_name='Sheet 1')
    read_file.to_csv(r'C:\xxxxxxxxx\xlwt summary.csv',index=None) #filepath and name.csv