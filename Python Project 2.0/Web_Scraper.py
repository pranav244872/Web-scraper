#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#reading the url
httpObject = urlopen("https://www.flipkart.com/search?q=graphics+card")
webdata = httpObject.read()

soup1 = soup(webdata)

pages_link = soup1.findAll('a',{'class':'ge-49M'})
domain = 'https://www.flipkart.com/search?q=graphics+card&page='
for i in range(2,11):
    link = domain+str(i)
    page_data = urlopen(link)
    webdata1 = page_data.read()
    webdata += webdata1
    
soupdata = soup(webdata, 'html.parser')

containers = soupdata.findAll('div',{'class':'_4ddWXP'})

print(type(containers),len(containers))

f = open('GraphicsCard.csv','wb')
f.write('ProductName,Stars,Rating,CurrentPrice,ImageURL \n'.encode())
for container in containers:
    #Finding product name
    product = container.findAll('a',{'class': 's1Q9rs'})
    ProductName = product[0].text.split(' Gr')[0]
    
    #Finding Stars
    star = container.find('div',{'class':'_3LWZlK'})
    try:
        Stars = star.text
    except:
        Stars = 0      
    
    #Finding Ratings 
    Rating = container.find('span',{'class':'_2_R_DZ'})
    try:
        Rating = Rating.text.replace('(','').replace(')','')
    except:
        Rating = 0
    
    #Finding Current Price
    CurrentPrice = container.find('div',{'class':'_30jeq3'}).text.replace(',','')
    
    #Finding Image
    ImageURL = container.img
    ImageURL = (ImageURL.get('src'))
    f.write(f"{ProductName},{Stars},{Rating},{CurrentPrice},{ImageURL}\n".encode())
    
f.close()