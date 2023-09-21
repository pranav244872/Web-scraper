#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('GraphicsCard.csv', error_bad_lines = False)
print(df)
#Graph
plt.figure(figsize=(20,14))
plt.bar(x=df["ProductName"],height=df['Rating'])
plt.title('Highest Rated Graphics Cards',fontsize = 15)
plt.xlabel('Graphics Card Names',fontsize = 15)
plt.ylabel('Number of People Rated',fontsize = 15)
plt.xticks(rotation=270,fontsize = 3)
plt.show()
#find the product having highest rating:
df[df['Rating']== max(df['Rating'])]