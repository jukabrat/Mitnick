import pyfiglet
import os
from colorama import Fore

class Main():
    def __init__(self):
        ascii_banner = pyfiglet.figlet_format("Mitnick")
        os.system("cls")
        print(Fore.LIGHTRED_EX+ascii_banner)
        print(Fore.WHITE+"opcije:")
        print(Fore.LIGHTYELLOW_EX+"cls - clearscreen, CTRL+C - exit(), exit - exit()")
        print("1. PenetrateDir")
        print("2. PenetrateSubdomain")
        print("3. port scan")
        print("4. DoRk")
        print("5. xsstrike [args -u link --crawl --proxy -h --json --fuzzer -level]")
        print("6. SQLI")
        print("7. BrutalniForcer")
        print("8. wafw00f [args url -h --verbose --findall --noredirect --proxy=PROXY(HTTP PROXY http://hostname:8080)]")
        print("9. ScrapeProxy [args --list]")
        print("10. ChromeProxy")
        print("11. info.txt")

        svi_infoi = ["BrutalniForcer/info.txt","penetrateDir/info.txt","penetrateSubdomain/info.txt","port_scan/info.txt","sqli/info.txt","wafw00f/info.txt","xsstrike/info.txt", ]
        print(Fore.WHITE+"\nupotreba: ")
        print(Fore.LIGHTBLUE_EX+"unosis redni broj programa koji pokreces, ako unosis i args za program onda ih pises pored rednog broja\n" + Fore.CYAN+"Zapoceo je session, to znaci kada ugasis program sve iz info.txt ce biti" +Fore.RED+" izbrisano!")
        try:
            opcija = input(Fore.WHITE+"\n"+"Izaberi: ")
        except KeyboardInterrupt:
            print("pozz")
            exit()
        while opcija != KeyboardInterrupt:
            if opcija == "":
                try:
                    print(Fore.LIGHTBLACK_EX+"unesi pravilno komadnu!")
                    opcija = input(Fore.WHITE+"\nIzaberi: ")
                except KeyboardInterrupt:
                    print("pozz")
                    exit()
            if opcija == "11":
                for i in svi_infoi:
                    with open(i) as file:
                        if len(file.read()) == 0:
                            pass
                        else:
                            print("\n")
                            print(Fore.WHITE+i.replace("/info.txt", "")+" Info: \n")
                            file.seek(0)
                            print(Fore.LIGHTBLACK_EX+file.read())
                            print("")
            elif opcija == "cls":
                Main()
            elif opcija == "exit":
                print("pozz")
                exit()
            elif opcija == "1" and len(opcija) == 1:
                print(Fore.LIGHTBLACK_EX+"Palim penetrateDir...")
                os.chdir("penetrateDir")
                os.system("start /wait cmd /k python main.py")
                os.chdir("..")
            elif opcija == "2" and len(opcija) == 1:
                print(Fore.LIGHTBLACK_EX+"Palim penetrateSubdomain...")
                os.chdir("penetrateSubdomain")
                os.system("start /wait cmd /k python main.py")
                os.chdir("..")
            elif opcija == "3" and len(opcija) == 1:
                print(Fore.LIGHTBLACK_EX+"palim port scan...")
                os.chdir("port_scan")
                os.system("start /wait cmd /k python main.py")
                os.chdir("..")
            elif opcija == "4" and len(opcija) == 1:
                print(Fore.LIGHTBLACK_EX+"Palim DoRk...")
                os.chdir("dork")
                os.system("start /wait cmd /k python main.py")
                os.chdir("..")
            elif opcija.startswith("5"):
                print(Fore.LIGHTBLACK_EX+"Palim xsstrike...")
                os.chdir("xsstrike")
                os.system("start /wait cmd /k python xsstrike.py " + opcija.replace("5", "") + " --log-file info.txt --file-log-level INFO")
                os.chdir("..")
            elif opcija == "6" and len(opcija) == 1:
                print(Fore.LIGHTBLACK_EX+"Palim SQLi...")
                os.chdir("sqli")
                os.system("start /wait cmd /k python main.py")
                os.chdir("..")
            elif opcija == "7" and len(opcija) == 1:
                print(Fore.LIGHTBLACK_EX+"Palim BrutalniForcer...")
                os.chdir("BrutalniForcer")
                print(Fore.RED+"\nBrutalniForcer :")
                print(Fore.LIGHTBLACK_EX+"1. HTTP-BRUTE")
                print(Fore.LIGHTBLACK_EX+"2. FTP-BRUTE")
                brutalniforcer = input(Fore.WHITE+"\nUnesi odabir (0 za nazad): ")
                if brutalniforcer == "1":
                    print(Fore.LIGHTBLACK_EX+"Palim HTTP-BRUTE")
                    os.system("start /wait cmd /k python main.py")
                elif brutalniforcer == "2":
                    print(Fore.LIGHTBLACK_EX+"Palim FTP-BRUTE")
                    os.chdir("ftp")
                    os.system("start /wait cmd /k python main.py")
                    os.chdir("..")
                elif brutalniforcer == "0":
                    pass
                os.chdir("..")
            elif opcija.startswith("8"):
                print(Fore.LIGHTBLACK_EX+"Palim wafw00f...")
                os.chdir("wafw00f/wafw00f/")
                os.system("start /wait cmd /k python main.py " + opcija[1:])
                os.chdir("../../")
            elif opcija.startswith("9"):
                if "--list" in opcija:
                    with open("checkproxy/proxylist.txt" , "r") as file:
                        lines = file.readlines()
                        print(Fore.LIGHTBLACK_EX+"zadnja sacuvana proxy lista: \n")
                        for line in lines:
                            print(line.strip())
                else:
                    print(Fore.LIGHTBLACK_EX+"Palim ProxyScrape...")
                    os.chdir("checkproxy")
                    os.system("start /wait cmd /k python checkproxy.py")
                    os.chdir("..")
            elif opcija == "10":
                print(Fore.LIGHTBLACK_EX+"Palim ChromeProxy...")
                os.chdir("ChromeProxy")
                os.system("start /wait cmd /k python main.py")
                os.chdir("..")
            else:
                print(Fore.LIGHTBLACK_EX+"unesi pravilno komandu!")
            try:
                opcija = input(Fore.WHITE+"\nIzaberi: ")
            except KeyboardInterrupt:
                print("pozz")
                exit()



if __name__ == "__main__":
    realcwd = os.getcwd()
    svi_infoi = ["BrutalniForcer/info.txt","penetrateDir/info.txt","penetrateSubdomain/info.txt","port_scan/info.txt","sqli/info.txt","wafw00f/info.txt","xsstrike/info.txt", ]
    open('info.txt', 'w').close()
    for i in svi_infoi:
        with open(i, "w") as file:
            file.write("")
            file.close()
    if realcwd == os.getcwd():
        pass
    else:
        os.system(realcwd)
    Main()