import requests 
from bs4 import BeautifulSoup 
import os
import time
import json

with open('') as file:
    settings = json.load(file)

URL = settings['url']
my_price = settings['budget']
headers = {"User-Agent": settings['user-agent']} 
currency_symbols = ['€', '£', '$', "¥", "HK$", "₹", "¥", ","] 

#Checking the price
def checking_price():
    page = requests.get(URL, headers=headers)
    soup  = BeautifulSoup(page.content, 'html.parser')

    if "amazon" in URL:
        try: 
            
            product_title = soup.find(id="productTitle").get_text().strip()
            product_price = soup.find(id="priceblock_ourprice").get_text()

    
            for i in currency_symbols : 
                product_price = product_price.replace(i, '')

            
            product_price = int(float(product_price))
            print("The Product Name is:" ,product_title.strip())
            print("The Price is:" ,product_price)


            if(product_price<my_price):
                result ="You Can Buy This Now!"
                print("You Can Buy This Now!")
                time.sleep(3) 
            else:
                result = "The Price Is Too High!"
                print("The Price Is Too High!")
            return  "Error! Not Available"
        except:
            result = "Error! Not Available"
            return result      

    elif "flipkart" in URL:
        try:
        
            product_title = soup.find(class_="B_NuCI").get_text().strip()
            product_price = soup.find(class_="_30jeq3 _16Jk6d").get_text()

    
            for i in currency_symbols : 
                product_price = product_price.replace(i, '')

            
            product_price = int(float(product_price))

    
            if(product_price<my_price):
                result ="You Can Buy This Product"+str(product_title)+" Now! The Price is "+str(product_price)+", which is under your budget!"
                
                time.sleep(3) 
            else: 
                result = "The Price of the product "+str(product_title)+" is "+str(product_price)+", Which is Too High, According to your budget !"
                
            return result
        except:
            result = "Error! Not Available"
            return result
    else:
        return "Vendor not recognized"


def run():
    while True:
        result = checking_price()
        print(result)
        return result
        

