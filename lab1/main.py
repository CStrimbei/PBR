pachet1 = ""
pachet2 = ""
pachet3 = ""
raspunsuripcht1 = ["", "", "", "", "", ""]
pcht1intrebari = [" ti-a placut cursul legat de inteligenta artificiala?", " ai vrea sa afli mai multe despre programarea bazata pe reguli?"," ti-a placut sa lucrezi in Java?", " ai vrea sa iti imbunatatesti cunostintele legate de platformele mobile?", " ti-au placut materiile legate de matematica?", " ai vrea sa faci ceva diferit?"]

for i in range(0, 6):
    print("Din experienta ta de pana acum," + pcht1intrebari[i])
    raspuns = input("Raspunsul tau (DA/NU):")
    raspunsuripcht1[i] = raspuns
PBR = 0
TPPM = 0
ACTN = 0
GD = 0
PSIHO = 0
CC = 0
IOC = 0
ARMS = 0
RPA = 0
SCA = 0
ISSA = 0
IIoT = 0

if raspunsuripcht1[0] == "DA":
    PBR = PBR + 1
if raspunsuripcht1[1] == "DA":
    PBR = PBR + 1
if raspunsuripcht1[2] == "DA":
    TPPM = TPPM + 1
if raspunsuripcht1[3] == "DA":
    TPPM = TPPM + 1
if(raspunsuripcht1[4] == "DA"):
    ACTN = ACTN + 1
if(raspunsuripcht1[5] == "DA"):
    GD = GD + 1

materii = {'Programare bazata pe reguli': PBR, 'Tehnici de programare pe platforme mobile': TPPM, 'Aspecte computationale in teoria numerelor': ACTN, 'Proiectarea Jocurilor': GD}

pachet1 = max(materii, key=materii.get)

print("Am inteles, alegerile tale au fost inregistrate.")

raspunsuripcht2 = ["", "", "", ""]

pcht2intrebari = [" ai vrea sa afli cum sa porti o comunicare adecvata in domeniul IT-ului?", " ai vrea sa afli mai multe despre programarea legata de cloud?", " ai vrea sa lucrezi pe domeniul interactiunii dintre om si calculator?", " ai vrea sa aprofundezi domeniul analizei datelor in cadrul retelelor sociale?"]

for i in range(0, 4):
    print("Din experienta ta de pana acum," + pcht2intrebari[i])
    raspuns = input("Raspunsul tau (DA/NU):")
    raspunsuripcht2[i] = raspuns

if raspunsuripcht2[0] == "DA":
    PSIHO = PSIHO + 1
if raspunsuripcht2[1] == "DA":
    CC = CC + 1
if raspunsuripcht2[2] == "DA":
    IOC = IOC + 1
if raspunsuripcht2[3] == "DA":
    ARMS = ARMS + 1

materii2 = {'Psihologia comunicarii in IT': PSIHO, 'Cloud Computing': CC, 'Interactiunea om calculator': IOC, 'Analiza datelor din retelele sociale': ARMS}

pachet2 = max(materii2, key=materii2.get)

print("Am inteles, alegerile tale au fost inregistrate.")

raspunsuripcht3 = ["", "", "", ""]

pcht3intrebari = [" ti-a placut cursul LFAC?", " ai vrea sa iti imbunatatesti cunostintele in legatura cu smart cardurile?", " ti-a placut cursul de inginerie software?", " ai vrea sa te familiarizezi cu conceptele legate de Internet of Things?"]

for i in range(0, 4):
    print("Din experienta ta de pana acum," + pcht3intrebari[i])
    raspuns = input("Raspunsul tau (DA/NU):")
    raspunsuripcht3[i] = raspuns

if raspunsuripcht3[0] == "DA":
    RPA = RPA + 1
if raspunsuripcht3[1] == "DA":
    SCA = SCA + 1
if raspunsuripcht3[2] == "DA":
    ISSA = ISSA + 1
if raspunsuripcht3[3] == "DA":
    IIoT = IIoT + 1

materii3 = {'Retele petri si aplicatii': RPA, 'Smart card-uri si aplicatii': SCA, 'Ingineria software specifica automobilelor': ISSA, 'Introducere in Internetul Lucrurilor': IIoT}

pachet3 = max(materii3, key=materii3.get)

print("Am inteles, alegerile tale au fost inregistrate.")

print("Pachetul 1 este: " + pachet1 + " conform alegerilor tale.")
print("Pachetul 2 este: " + pachet2 + " conform alegerilor tale.")
print("Pachetul 3 este: " + pachet3 + " conform alegerilor tale.")
