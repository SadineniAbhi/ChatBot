import requests
from bs4 import BeautifulSoup
from crawlers.writeDataToFile import write_data
from crawlers.loggerFile import logger
from crawlers.zipper import zip_folder
import os 

def scrape_website(url):
    url_lis = []
    url_lis.append(url)
    visited_urls =set()
    i = 0


    while i<len(url_lis):
        try:
            if url_lis[i][0:5] != "https":
                continue
            
            response = requests.get(url_lis[i])
            visited_urls.add(url_lis[i])

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                anchor_elements = soup.find_all('a')
                for element in anchor_elements:
                    href=element.get('href')
                    if href and href not in visited_urls:
                        url_lis.append(href)
                all_text = soup.get_text()
                write_data(all_text)

            else:
                  
                  logger.warning("No data found at URL: %s", url_lis[i])
            print(*url_lis)
            i+=1

        
        except Exception as e:
            logger.error("An exception has occurred while scraping %s: %s", url_lis[i], e)
            i+=1
            continue



        folder_path  = os.path.dirname(os.path.abspath(__file__))+'/data'
        zip_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/zipeddata'
        zip_folder(folder_path, zip_path)

