import pyfiglet
import os
import webbrowser

class Main():
    def __init__(self):
        os.system("cls")
        ascii_banner = pyfiglet.figlet_format("DoRk")
        print(ascii_banner)
        self.dorklist = []
        self.dorklistweb = []
        self.rb = 0
        dork = input("Dork kategorija (0): ")
        if dork == "0":
            os.chdir("..")
            os.system("python main.py")
        file = open("dorks.txt")
        content = file.readlines()

        self.dorkcategory(content, dork)
        kategorija = input("Izaberi kategoriju: ")
        self.rb = 0
        self.printdorks(content, kategorija)
        print("komande: sve, (lista) ex.2,5,1,6 ili jedan broj")
        pokreni = input("komanda: ")
        self.pokreni(pokreni)

        ponovi = input("ponovo pokreni program? da/ne: ")
        if ponovi == "da":
            Main()
        else:
            exit()
    def dorkcategory(self, content, dork):
        for i in range(0, len(content)):
            if dork.lower() in content[i]:
                if "# Category" in content[i]:
                    self.rb +=1
                    print(str(self.rb) + ". " +  str(content[i]))
                    self.dorklist.append(i)
                else:
                    pass
            elif dork.upper() in content[i]:
                if "# Category" in content[i]:
                    self.rb +=1
                    print(str(self.rb) + ". " +  str(content[i]))
                    self.dorklist.append(i)
                else:
                    pass
            elif dork.capitalize() in content[i]:
                if "# Category" in content[i]:
                    self.rb +=1
                    print(str(self.rb) + ". " +  str(content[i]))
                    self.dorklist.append(i)
                else:
                    pass
    
    def printdorks(self, content, kategorija):
        for l in range(self.dorklist[int(kategorija)-1], 50000):
            if len(content[l]) == 1:
                break
            elif "# Category" in content[l]:
                print(content[l])
                pass
            else:
                self.rb += 1
                print(str(self.rb) + ". "+ content[l])
                self.dorklistweb.append(content[l])
            

    def pokreni(self, pokreni):
        if "sve" in pokreni:
            for dork in self.dorklistweb:
                webbrowser.open_new_tab("https://www.google.com/search?q=" + dork)
        else:
            pokreni.split(sep=",")
            for broj in pokreni.split(sep=","):
                webbrowser.open_new_tab("https://www.google.com/search?q=" + self.dorklistweb[int(broj)-1])


if __name__ == "__main__":
    Main()