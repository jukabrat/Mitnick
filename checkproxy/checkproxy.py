import requests
from concurrent.futures import ThreadPoolExecutor
import os
import webbrowser
from pyfiglet import figlet_format
from time import sleep

class Main():
    def __init__(self):
        os.system("cls")
        logo = figlet_format("ProxyScrape")
        print(logo)
        github = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
        webbrowser.open_new("https://advanced.name/freeproxy?type=https")
        link = input("link proxya sa advanced.name: ")
        dane = input("check i proxye sa githuba? da/ne: ")
        try:
            r = requests.get(link)
        except:
            print("Link ne radi! pokusaj ponovo!")
            sleep(2)
            Main()
        try:
            proxies = str(r.content).split(sep="\\r\\n")
        except:
            pass
        
        if len(proxies) == 1:
            print("Link koji si ukucao ne radi...")
            print("pokusaj ponovo")
            sleep(2)
            Main()
        else:
            if dane == "da":
                r2 = requests.get(github)
                proxiesgit = str(r2.content).split(sep="\\n")
                for proxygit in proxiesgit:
                    proxies.append(proxygit)
            print("Link radi! Pocinjem proxylist")
            print("Nakon sto sakupi dovoljno proxija mozete samo ugasiti ovaj prozor i nastaviti program")
            f = open('proxylist.txt', 'r+')
            f.truncate(0)
            self.rb = 0
            with ThreadPoolExecutor(100) as self.exe:
                for proxy in proxies:
                    try:
                        self.exe.submit(self.checkport, proxy)
                    except KeyboardInterrupt:
                        self.exe.shutdown(wait=False, cancel_futures=True)
            

    def checkport(self, proxy):
        probajproxy = {
                "https": ""
            }
        probajproxy["https"] = "http://"+proxy
        try:
            requests.get("https://google.com", headers={"Content-Type":"text"},proxies=probajproxy, timeout=20)
            self.rb +=1
            print(str(self.rb) + ". radi proxy: " + proxy)
            with open("proxylist.txt", "a") as file:
                file.write(proxy + "\n")
        except:
            pass
if __name__ == "__main__":
    Main()