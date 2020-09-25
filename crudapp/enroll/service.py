from service_objects.services import Service
from bs4 import BeautifulSoup
import requests

class Product:
    ItemTitle=''
    Description=''
    Brand=''
    ItemModel=''
    ItemOrigin=''
    ImageUrl=''

class ScrappingService(Service):
    def get_amazon_data(self):
        list = ['iPhone', 'Apple Watch', 'Headphones']
        return list

    def get_ebay_laptops(self):
        ebay_url="https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=laptop&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=mobile"
        source = requests.get(ebay_url).text
        soup = BeautifulSoup(source, 'lxml')
        all_products=[]
        items = soup.find_all('li', class_='s-item')
        for item in items:

            eachItem=Product()
            try:
                eachItem.ItemTitle=item.find('h3', class_='s-item__title').text
            except Exception as e:
                eachItem.ItemTitle = 'None'

            try:
                eachItem.ImageUrl=item.find('img', class_='s-item__image-img')['src']
            except Exception as e:
               eachItem.ImageUrl = 'None'

            try:
               eachItem.Brand=item.find('span', class_='s-item__dynamic s-item__dynamicAttributes1').text.split(' ')[1]
            except Exception as e:
               eachItem.Brand = 'None'

            all_products.append(eachItem)

        
        return all_products
            
            
