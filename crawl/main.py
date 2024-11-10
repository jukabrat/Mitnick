from bs4 import BeautifulSoup as bs
import requests
from concurrent.futures import ThreadPoolExecutor

class Main():
    def __init__(self):
        self.links = []
        host = "http://testphp.vulnweb.com/login.php"
        r = requests.get(host)
        self.soup = bs(r.text, 'html.parser')
        self.crawlpocetna()
        

    def crawlpocetna(self):
        tittles = self.soup.find_all('a', href=True)
        for tittle in tittles:
            if tittle in self.links:
                pass
            else:
                self.links.append(tittle)

    def crawldalje(self):
        soup = bs(r.text, 'html.parser')
        for link in self.links:
            if 
        soup = bs(r.text, 'html.parser')



if __name__ == "__main__":
    Main()


