from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv 

url=("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
Chro=webdriver.Chrome("C:\\Users\\Bhavy\Documents\\python1\\C-127 Project\\chromedrive_win32\\chromedriver.exe")
Chro.get(url)
time.sleep(12)
def Starr():
    Headers=["Proper name","Distance","Mass","Radius"]
    bright=[]
    for i in range(1):
        soup=BeautifulSoup(Chro.page_source,"html.parser")
        for ultag in soup.find_all('tr',attrs={"class","Proper Name"}):
          atags=ultag.find_all("td")
          carrlist=[]
          for  index, a_tago in enumerate(atags):
            if index==0:
                carrlist.append(atags.find_all("a")[0].contents[0])
            else:
               try:
                 carrlist.append(a_tago.content[0])
               except:
                  carrlist.append("")
            bright.append(carrlist) 
    with open("theoutput.py","w")as f:
       csvwriter= csv.writer(f)
       csvwriter.writerow(Headers)
       csvwriter.writerows(bright) 
Starr()
    