from service_objects.services import Service
from bs4 import BeautifulSoup


class ScrappingService(Service):
    def get_amazon_data(self):
        list = ['iPhone', 'Apple Watch', 'Headphones']
        return list
