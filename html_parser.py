import requests
import codecs
import urllib.request
import time
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re
import os

#input
Result_File="report.txt"

#deleting result file if exists
if os.path.exists(Result_File):
  os.remove(Result_File)

#reading html file and parsing logic
f=codecs.open("test.html", 'r', 'utf-8')
xhtml = f.read()
data = []
# instantiate the parser and feed data to it
soup = BeautifulSoup(xhtml,"html.parser")
#print(soup)
main_table = soup.find('table', { 'id': 'octable' })
#print(main_table)
with open(Result_File, 'w') as r:
    r.write("OI_CE|Chng_in_OI_CE |Volume_CE|IV_CE|LTP_CE|NetChng_CE|Bid_Qty_CE|Bid_Price_CE|Ask_Price_CE|Ask_Qty_CE|StrikePrice|Bid_Qty_PE|Bid_Price_PE|Ask_Price_PE|Ask_Qty_PE|Net_Chng_PE|LTP_PE|IV_PE|Volume_PE|Chng_in_OI_PE|OI_PE")
    for rows in main_table.find_all('tr'):
     for cell in rows.find_all('td'):

#print(data)
        if(len(cell.text) != 0):
         cell_text = cell.text.strip()
         a = re.sub(r"\n", "", cell_text, 0)

         r.write(a)
         r.write("|")
     r.write("\n")




