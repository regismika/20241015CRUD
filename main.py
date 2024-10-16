
automobiliai = [{"marke": "Honda", "modelis": "Accord", "metai": 2009, "pavara": "FWD"},
    {"marke": "Jeep", "modelis": "Grand Cherokee", "metai": 2002, "pavara": "AWD"}]

def printInfo():
    print("\nAutomobilių valdymo sistema")
    print("1. Peržiūrėti automobilius")
    print("2. Pridėti automobilį")
    print("3. Redaguoti automobilį")
    print("4. Ištrinti automobilį")
    print("5. Išeiti iš programos")
    print("-----------------------------")

def printAutomobilis(auto, num):
    print(f"{num}. Marke: {auto['marke']}, Modelis: {auto['modelis']}, Metai: {auto['metai']}, Pavara: {auto['pavara']}")

# Funkcija peržiūrėti sąrašą
def printAutomobiliai():
    num = 1
    for auto in automobiliai:
        printAutomobilis(auto, num)
        num += 1
    print(f"Automobilių skaičius sąraše: {num - 1}")

# Pridėti
def addAutomobilis():
    marke = input("Markė: ")
    modelis = input("Modelis: ")
    metai = int(input("Gamybos metai: "))
    pavara = input("Pavara (FWD/AWD/RWD): ")
    automobiliai.append({"marke": marke, "modelis": modelis, "metai": metai, "pavara": pavara})
    print(f"Automobilis {marke} {modelis} pridėtas.")

# Redagavimas
def editAutomobilis():
    ed = int(input("Įveskite automobilio numerį, kurį norite redaguoti: ")) - 1
    if 0 <= ed < len(automobiliai):
        print("Nauji duomenys:")
        marke = input("Nauja markė: ")
        modelis = input("Naujas modelis: ")
        metai = int(input("Nauji gamybos metai: "))
        pavara = input("Nauja pavara (FWD/AWD/RWD): ")
        automobiliai[ed] = {"marke": marke, "modelis": modelis, "metai": metai, "pavara": pavara}
        print("Automobilis atnaujintas.")
    else:
        print("Tokio automobilio nėra")

# Deletinimas
def removeAutomobilis():
    rem = int(input("Įveskite automobilio numerį, kurį norite pašalinti: ")) - 1
    if 0 <= rem < len(automobiliai):
        automobiliai.pop(rem)
        print("Automobilis ištrintas.")
    else:
        print("Tokio automobilio nėra")

# Programa
print("---- AUTOMOBILIŲ DUOMENŲ BAZĖ ----")
while True:
    printInfo()
    opt = int(input("Pasirinkite veiksmą: "))
    match opt:
        case 1:
            printAutomobiliai()
        case 2:
            addAutomobilis()
        case 3:
            editAutomobilis()
        case 4:
            removeAutomobilis()
        case 5:
            exit(1)
        case _:
            print("Neteisingas pasirinkimas, bandykite dar kartą.")
