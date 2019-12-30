import requests
import codecs
import urllib.request
import time
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re
import os
import pandas as pd
import sys
#input
input_html_file_name = sys.argv[1]
Result_File = sys.argv[2]
final_result_file = sys.argv[3]

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
        if(len(cell.text) != 0):
         cell_text = cell.text.strip()
         cell_value = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", cell_text, 0)
        # (r"\n\t\r", "", cell_text, 0)
         r.write(cell_value)
         r.write("|")
     r.write("\n")


pattern = re.compile(r'<span>As on (.+?) IST<a>')
data_collection_time = pattern.findall(str(soup))[0]
pattern = re.compile(r'Underlying Index: <b style="font-size:1.2em;">NIFTY (.+?)<\/b>')
nifty_base_price = pattern.findall(str(soup))[0]

#print(data_collection_time)

data_as_csv = pd.read_csv(Result_File, encoding='ISO-8859\xe2\x80\x931',sep='|', index_col=False)
data_as_csv['data_collection_time'] = str(data_collection_time)
data_as_csv['nifty_base_price'] = str(nifty_base_price)
data_as_csv = data_as_csv.drop('Ask_Price_CE', 1)
data_as_csv = data_as_csv.drop('Ask_Price_PE', 1)
data_as_csv = data_as_csv.drop('Ask_Qty_CE', 1)
data_as_csv = data_as_csv.drop('Ask_Qty_PE', 1)
data_as_csv = data_as_csv.drop('Bid_Price_CE', 1)
data_as_csv = data_as_csv.drop('Bid_Price_PE', 1)
data_as_csv = data_as_csv.drop('Bid_Qty_CE', 1)
data_as_csv = data_as_csv.drop('Bid_Qty_PE', 1)
data_file_contains_prev_data = pd.read_csv(final_result_file, encoding='ISO-8859\xe2\x80\x931',sep='|', index_col=False)

#data_file_contains_prev_data.append(data_as_csv,ignore_index = True)
#print(str(data_as_csv))

data_file_contains_prev_data = data_file_contains_prev_data.append(data_as_csv, ignore_index=True)
data_file_contains_prev_data.to_csv(final_result_file, index=False, sep='|')
    



