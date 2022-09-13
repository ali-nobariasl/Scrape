from bs4 import BeautifulSoup 
import requests
import pandas 

class Scraper:
    
    @classmethod
    def scrape(cls):
        site = input("Enter your url please: \n")
        link_list = []
    
        page = requests.get(site)
        page_encoding = page.__getattribute__('encoding')
        page_status = page.__getattribute__('status_code')
        page_elapsed = page.__getattribute__('elapsed')
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            link_list.append(link_address)    
    
        data_frame = pandas.DataFrame({
            'page_encoding': page_encoding,
             'page_status': page_status,
            'page_elapsed': page_elapsed,
            'links': link_list
    })
    
        return data_frame



print(Scraper.scrape())


#"https://www.google.com"
#https://www.imdb.com