import requests
from bs4 import BeautifulSoup
from .CustomError import CustomError
from .writeDataToFIle import write_data

def scrape_website(url):
    url_lis = []
    url_lis.append(url)
    i = 0
    while i<len(url_lis):
        try:
            if url_lis[i][0:5] != "https":
                url_lis[i] = url_lis[0]+url_lis[i]
            print(url_lis[i])
            response = requests.get(url_lis[i])
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                anchor_elements = soup.find_all('a')
                for element in anchor_elements:
                    href=element.get('href')
                    url_lis.append(href)
                all_text = soup.get_text()
                write_data(all_text)
            else:
                raise CustomError("No data found")
            i+=1
        except Exception as e:
            print("An exception has ocured while scrapping",url_lis[i])
            i+=1
            continue
    

