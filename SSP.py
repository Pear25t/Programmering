import random

ro=["Sten", "Sax", "Påse"]

spoäng=0
dpoäng=0

while spoäng < 3 and dpoäng < 3:

    ssp = input()

    dator_val = random.choice(ro)

    print(dator_val)

    if ssp == dator_val:
        print("Lika")

    elif ssp == "Sten" and dator_val == "Sax":
        spoäng += 1
        print("Spelare van")
        print("Din poäng", spoäng)

    elif ssp == "Sax" and dator_val == "Påse":
        spoäng += 1
        print("Spelare van")
        print("Din poäng", spoäng)

    elif ssp == "Påse" and dator_val == "Sten":
        spoäng += 1
        print("Spelare van")
        print("Din poäng", spoäng)

    else:
        dpoäng += 1
        print("Dator van")
        print("Datorns poäng", dpoäng)
