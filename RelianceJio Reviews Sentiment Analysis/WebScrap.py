import requests
import re
from bs4 import BeautifulSoup
import csv

print("GOOGLING....")


outfile = open('/Users/shreyas_rl/Desktop/Reliance-Industries-Ltd-Internship/Web Scrap + Sentiment Analysis/data.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(["id", "desc"])

i = 1
for pgno in range(2,101):
	website = "https://www.consumercomplaints.in/?search=reliance+jio&sort-type=relevance&page="+str(pgno)

	print(website)
	page = requests.get(website)

	soup = BeautifulSoup(page.text, 'html.parser')

	for item in soup.find_all("td", attrs = {'class':'complaint'}):
		#print(item)
		for subitem in item.find_all('a'):
			id = i
			desc = subitem['href']
			writer.writerow([id, desc[1:]])
			#print(id)
			i = i+1




'''for itemname in soup.find_all("img", attrs = {'class':'store_logo impressions_gts lazy img_alt'}):
		itemnames.append(itemname['alt'])
for itemprice in soup.find_all("span", attrs = {'class':'store_prc'}):
		itemprices.append(itemprice['data-price'])

for i,j in zip(itemnames,itemprices):
	print(i, j)'''

	
'''for item in soup.find_all("span", attrs = {'class':'store_prc'}):
	print(item['data-price'])'''


#<div style="margin: 7px 0;">
                                    
#<span class="store_prc" data-price="22990">Rs. 22,990<small class="price_price_small">.00</small>
                                                                                    
'''for price in soup.find_all("span", attrs = {'class':"a-price-whole"}):
	print(price)

https://www.91mobiles.com/vivo-v17-price-in-india'''

#<span class="a-price-whole">76,900</span>


'''search_results = requests.get("https://www.google.com/search?q="+user_input+' price')

soup = BeautifulSoup(search_results.text, 'html.parser')
#print(soup.prettify())
for link in soup.find_all("a",attrs = {'href': re.compile('https://')}):
	r = link.get('href')
	r = r[7:]
	#print(r)
	if r[:4] == 'http':
		print(r)
		search = requests.get(r)
		soup2 = BeautifulSoup(search.text,'html.parser')
		print(soup2.prettify())'''
		
#find_all('_prcin', attrs = {'id':'priceinindia'}