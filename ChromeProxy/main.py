import requests
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
from selenium import webdriver
from time import sleep
import os
import pyfiglet

class Main():
    i = 0
    proxyrb = 1
    def __init__(self):
        ascii_banner = pyfiglet.figlet_format("ChromeProxy")
        print(ascii_banner)
        self.ua = UserAgent()
        self.proxylist = []
        os.system("start /wait cmd /k python ../checkproxy/checkproxy.py")
        print("\nide proxy hierarhija!")
        with open("proxylist.txt", "r") as file:
            lines = file.readlines()
            os.chdir("../ChromeProxy/")
            with ThreadPoolExecutor(50) as exe:
                for line in lines:
                    exe.submit(self.proxyhierarchy, line.strip())
        self.salji()

    def salji(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=http://%s' % self.proxylist[Main.i].strip())
            chrome_options.add_experimental_option("detach", True)
            chrome = webdriver.Chrome(options=chrome_options)
            chrome.get("https://dnsleaktest.com")
        except:
            print("proxy Timed out" + self.proxylist[Main.i])
            Main.i += 1
            print("mijenjam u proxy " + self.proxylist[Main.i])

    def proxyhierarchy(self, line):
        proxy = {
            "https":""
        }
        proxy["https"] = "http://"+line
        try:
            r = requests.get("https://google.com", proxies=proxy, headers={"content-type":"text"}, timeout=20)
            print(str(Main.proxyrb) + ". " + line)
            self.proxylist.append(line)
            Main.proxyrb+=1
        except:
            pass


if __name__ == "__main__":
    Main()