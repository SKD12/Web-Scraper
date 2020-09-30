#import bs4
#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

my_url_1='https://orangehousing.com/index.php/syracuse-apartments/listings'
r=requests.get(my_url_1)
print(r.status_code)
#check status code if 403 or 503 then it's an error, we need to sort it or else if status code 200 then we are good to go.

headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
#headers is used so as to avert an error because many websites block access while scraping



#my_url='https://www.rent.com/new-york/syracuse-university/apartments_condos_houses_townhouses'
#ALL RESULTS FOR 2 BED AND 2 BATHROOM
#RENT= <span class="altRentDisplay">$2,000 - 2,200</span>
#NAME= <a class="placardTitle js-placardTitle  " href="https://www.apartments.com/pike-block-syracuse-ny/9tkebf5/" title="Pike Block, Syracuse, NY">
#Pike Block</a>
#ADDRESS= <div class="location" title="300 S Salina St, Syracuse, NY 13202">300 S Salina St, Syracuse, NY 13202</div>
uClient=requests.get(my_url_1, headers=headers)

#page_html=uClient.res.text()
#uClient.close()

orange_soup = soup(uClient.content, "html.parser")

#container=page_soup.findall("div" ,{"class":"propertyInfo"})
print(len(orange_soup))
XYZ = orange_soup.find("table", {"id": "table_id"})
print(len(XYZ))
f = open("file name", "a")
print(XYZ.find("href"), file=f)
f.close()
#for finding details refer to the class and
#XYZA= XYZ.find_all("tbody",{"class": "dtr-details"})


#container_1=orange_soup.findAll("tr" , {"class" : "child"})
"""container_1 = orange_soup.findAll("div", {"class":"child"})
print(len(container_1))"""