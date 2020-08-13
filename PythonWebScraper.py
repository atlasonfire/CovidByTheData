from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import winsound
import csv


#stream for output file
output = open('C:/ScriptsTemp/JasonPlayground/WebScraper/data/output.csv','w',newline='')

#declare csv writer
writer = csv.writer(output)

#configure the selenium web driver for Chrome browser
driver = webdriver.Chrome("C:/ScriptsTemp/Selenium Drivers/Chrome/Chrome81/chromedriver.exe")

#Create data sets
dates=[]
currentTravelers=[]
previousTravelers=[]

#get the website
driver.get("https://www.tsa.gov/coronavirus/passenger-throughput")

#transfer content from selenium to beautifulsoup
content = driver.page_source
soup = BeautifulSoup(content)

#print(soup)

#find the table elements
for mytable in soup.findAll('table'):
        for trs in mytable.find_all('tr'):
                tds = trs.find_all('td')
                #print(tds)
                row = [elem.text.strip().encode('utf-8') for elem in tds]
                row = [str(e) for e in row]
                row = [t[1:] for t in row]
                row = [r.replace('\'','') for r in row]
                if not row:
                        continue
                print(row)
                writer.writerow(row)

output.close()
print('Done!')
winsound.Beep(850,2000)
                
