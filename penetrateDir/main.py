import requests
from concurrent.futures import ThreadPoolExecutor
import os
import pyfiglet

class Main():
    linenum = 0
    mjesto = 1
    iter = 0
    i = 0
    def __init__(self):
        ascii_banner = pyfiglet.figlet_format("penetrateDir")
        print(ascii_banner)
        print("Ako program sa proxyima bude bez seckanja i prebrzo radio znaci da najvjerovatnije proxy ne radi i treba ugasiti program ODMAH, jer niti su proxy dobri niti je program toliko brz!")
        self.proxylista = []
        self.ok = []
        self.pr = []
        self.auth = []
        self.ostalo = []
        self.host = input("Host (bez kosih crtica na kraju!: 0): ")
        if self.host == "0":
            os.chdir("..")
            os.system("python main.py")

        os.chdir("wordlists")
        print("\n Wordlists: \n")
        os.system("dir /b")
        os.chdir("..")
        print("\n")

        self.wordlista = input("Wordlist: ")
        self.stapise = input("sta pise kada odes na neki dio stranice koji ne postoji (enter za nista): ")

        self.proxylist = input("Proxy? da/ne: ")
        
        
        if self.proxylist == "da":
            os.system("start /wait cmd /k python checkproxy.py")
            with open("proxylist.txt", "r") as file:
                lajns = file.readlines()
                print("Pravim hierarhiju najboljih proxija!... sacekajte")
                with ThreadPoolExecutor(len(lajns)) as exe:
                    for line in lajns:
                        exe.submit(self.proxyhierarchy, line)
            self.radnici = input("Broj radnika (treba biti veci od broja proxya! (" + str(len(self.proxylista)) + "): ")
            print("Gotovo!")
            self.wordlist = open("wordlists/"+self.wordlista, "r")
            lines = self.wordlist.readlines()
            self.linelen = len(lines)
            print("Proxy lista je spremna!")
            print("\nKoristim proxy: " + self.proxylista[Main.i] + "\n")
            with ThreadPoolExecutor(int(self.radnici)) as exe:
                for line in lines:
                    Main.linenum +=1
                    exe.submit(self.penetrateproxy, line , Main.linenum)
                        
            self.wordlist.close()
            self.rezultati()
        else:
            self.radnici = input("Broj radnika (treba biti veci od broja proxya!): ")
            inputproxy = ""
            self.wordlist = open("wordlists/"+self.wordlista, "r")
            lines = self.wordlist.readlines()
            self.linelen = len(lines)
            with ThreadPoolExecutor(int(self.radnici)) as exe:
                for line in lines:
                    Main.linenum +=1
                    exe.submit(self.penetrate, line, Main.linenum)
            self.wordlist.close()
            self.rezultati()
        

        
    def penetrate(self, line, linenum):
        try:
            r = requests.get(self.host + "/" + line, timeout=20, allow_redirects=True)
        except requests.exceptions.Timeout:
            pass
        if len(self.stapise) == 0:
            if r.status_code == 200:
                self.ok.append(self.host + "/" + line.strip() + ": " + str(r.status_code) + " OK\n")
            elif r.status_code == 401:
                self.pr.append(self.host + "/" + line.strip() + ": " + str(r.status_code) + " UNAUTHORIZED\n")
            elif r.status_code == 402:
                self.auth.append(self.host + "/" + line.strip() + ": " + str(r.status_code) + " Payment Required\n")
            else:
                pass
        else:
            if self.stapise not in str(r.content):
                self.ok.append(self.host + "/" + line.strip() + ": " + str(r.status_code) + " OK\n")
        
        print(str(linenum) +"/"+ str(self.linelen), end='\r', flush=True)


    def penetrateproxy(self, line, linenum):
        inputproxy = self.proxylista[Main.i]
        proxy = {
            "https": ""
        }
        proxy["https"] = "http://"+inputproxy
        if self.proxylist == "da":
            try:
                if linenum == 1:
                    r2 = requests.get("https://dnsleaktest.com" , proxies=proxy)
                    print(str(r2.content) + "\n")
                url = self.host + "/" + line.strip() + "/"
                r = requests.get(url, proxies=proxy, timeout=20, allow_redirects=True)
                if len(self.stapise) == 0:
                    if r.status_code == 200:
                        self.ok.append(url + ": " + str(r.status_code) + " OK\n")
                    elif r.status_code == 402:
                        self.auth.append(url + ": " + str(r.status_code) + " Payment Required\n")
                    elif r.status_code == 401:
                        self.pr.append(url + ": " + str(r.status_code) + " UNAUTHORIZED\n")
                else:
                    if self.stapise not in str(r.content):
                        self.ok.append(url + ": " + str(r.status_code) + " OK\n")
            except:
                Main.iter += 1
                if Main.iter == int(self.radnici):
                    Main.i += 1
                    Main.iter = 0
                    print(self.proxylista[Main.i-1] + " Timed out")
                    print("Mijenjam u proxy: " + self.proxylista[Main.i])
                    r2 = requests.get("https://dnsleaktest.com" , proxies={"https": self.proxylista[Main.i]})
                    print(str(r2.content) + "\n")

        
        
        print(str(linenum) +"/"+ str(self.linelen), end='\r', flush=True)


    def proxyhierarchy(self,line):
        probajproxy = {
            "https": ""
        }
        probajproxy["https"] = "http://"+line
        req = requests.get("https://google.com",headers={"Content-Type":"text"}, proxies=probajproxy, timeout=20)
        print(str(Main.mjesto)+". " + str(line.strip()) + " - " + str(req.status_code))
        Main.mjesto +=1
        self.proxylista.append(line.strip())
    

    def rezultati(self):
        file = open("info.txt", "w")
        print("Gotovo")
        print("Rezultati: \n")
        print("OK 200: \n")
        file.write("\n"+"OK 200: \n")
        for o in self.ok:
            print(o)
            file.write(o)
        print("\nPayment Required 402: \n")
        file.write("\n"+"Payment required 402: \n")
        for p in self.pr:
            print(p)
            file.write(p)
        print("\nUNAUTHORIZED 401: \n")
        file.write("\n"+"UNAUTHORIZED 401: \n")
        for p2 in self.pr:
            print(p2)
            file.write(p2)


if __name__ == "__main__":
    os.system("cls")
    Main()