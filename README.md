<b>Proces instalacije Mitnick (Windows)</b>

<b>Program za sada radi samo na sistemu Windows</b>.

1. Instalirati sve dokumente iz repostorijuma i ubaciti u jedan folder
2. Nakon toga <b>"pip3 install -r requirements.txt"</b> da instalirate sve biblioteke koje su se koristile za ovaj projekat
3. Tada mozete pokrenuti glavni </b>python main.py</b> program


<b>Koristenje programa</b>

glavni menu je jednostavan imate prompt u koji unosite opciju koji program zelite da pokrenete, taj program se zapocinje u novom cmd promptu i trazi vam input koji najbolje detaljno procitajte

postoji 10 programa od kojih su 8 moji a 2 su preuzeta sa githuba, to su XSStrike i Wafw00f.
postoji i 11. opcija koja se zove "info.txt" tu ce se sacuvati sve informacije koje su vam ostali programi ispisali, npr. ako uđete u XSStrike i obavite skeniranje, nakon sto izađete, output koji vam je XSStrike dao ce se sacuvati u info.txt dok ne ugasite glavni program main.py

<b>Opis programa:</b>

1. penetrateDir trazi unos hosta i obavezno bez kose crte na kraju, ponudit ce vam vise wordlisti i mogucnost koristenja proxya koji je automatizovan, to znaci da ne morate imati svoj proxy vec on pronalazi najbolji.
2. penetrateSubdomain radi na isti princip kao i penetradeDir samo sto u ovom promptu ne smijete unositi bilo kakav subdomain koji je vec u linku,  to podrazumijeva www.
3. portScan skenira portove i isto nudi automatizovano pronalazanje proxya samo sto nakon sto pronađe proxy potrebno je da kopirate neki od proxya i zalijepite u input kada budete ugasili program za pronalazenje proxya
4. Dork trazi jednu ili maksimalno dvije rijeci za pretrazivanje najboljih dokrova, nakon sto ih pronađe vrati vam informaciju i nudi da izaberete jedan redni broj koji zelite da otvori na Googlu.
5. XSStrike je program za pronalazenje i eksploitaciju ranjivosti na web serveru, program moze da pretrazi citavu webstranicu ili samo jedan page za ranjivosti XSS, koristite ga tako sto unesete broj 5 i nakon toga ostale argumente
6. SQLi trazi dva unosa sa linkom, jedan link je na kojem je postavljena forma, a na drugom linku je gdje se koristi post methoda za slanje obrasca, kada unesete ta dva inputa trazit ce vam wordlist, unos podataka iz forme i mogucnost koristenja proxya
7. BrutalniForcer za sada ima samo dvije opcije, HTTP-BRUTE i FTP-BRUTE, u prvoj opciji napada se login forma pomocu wordlisti, radi na slican princip kao SQLi, FTP-Brute napda ranjive FTP login portove
8. Wafw00f pronalazi WAF na web stranici to jeste web application firewall i koja je verzija WAF-a
9. Scrapeproxy je program koji pronalazi proxye na internetu, kao i ostai programi u Mitnicku koji koriste proxy, ovaj program ce otvoriti advanced.name link i traziti da generisete link sa te webstranice i unesete ga u program, nakon toga ako vam treba vise proxya mozete koristiti opciju za github
10. Chromeproxy pronalazi proxye i nakon toga pokrece Chrome koji radi na proxyu tako da je vasa ip addresa sakrivena i svi podaci idu kroz taj proxy
11. info.txt je file u kojem je sacuvan svaki od outputa ovih programa, koji mozete otvoriti u glavnom meniju ako zelite necega da se podsjetite

program je napravljen amaterski, tako da ako bude bugova, prijavite.

