import random
import collections
import os

kort = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "1"]

spelare1 = []
spelare2 = []
spelare3 = []

spelare1poäng = 0
spelare2poäng = 0
spelare3poäng = 0

spelare_tur = 1

def check_kort():
    global spelare1poäng, spelare2poäng, spelare3poäng
    spelare1_counter=collections.Counter(spelare1)
    spelare2_counter=collections.Counter(spelare2)
    spelare3_counter=collections.Counter(spelare3)
    for kort in spelare1_counter:
        if spelare1_counter[kort] == 4:
            spelare1poäng += 1
            spelare1.remove(kort)            
            spelare1.remove(kort)            
            spelare1.remove(kort)            
            spelare1.remove(kort)
    for kort in spelare2_counter:
        if spelare2_counter[kort] == 4:
            spelare2poäng += 1
            spelare2.remove(kort)            
            spelare2.remove(kort)            
            spelare2.remove(kort)            
            spelare2.remove(kort)        
    for kort in spelare3_counter:
        if spelare3_counter[kort] == 4:
            spelare3poäng += 1
            spelare3.remove(kort)            
            spelare3.remove(kort)            
            spelare3.remove(kort)            
            spelare3.remove(kort)


for i in range (7):
    random_kort = random.choice(kort)
    spelare1.append(random_kort)
    kort.remove(random_kort)

for i in range (7):
    random_kort = random.choice(kort)
    spelare2.append(random_kort)
    kort.remove(random_kort)

for i in range (7):
    random_kort = random.choice(kort)
    spelare3.append(random_kort)
    kort.remove(random_kort)


while len(spelare1) != 0 and len(spelare2) != 0 and len(spelare3) != 0:
    while True:
        os.system("cls")
        if len(spelare1) == 0:
            random_kort = random.choice(kort)
            spelare1.append(random_kort)
            kort.remove(random_kort)
        
        print("Du har", spelare1poäng, "Par")
        print("Välj ett kort", spelare1)    
        kort_val = input()

        if kort_val not in spelare1:
            print("Du har inte detta kort")
            continue

        print("välj en spelare")
        spelar_val = input()

        

        if spelar_val == "2":
            if kort_val in spelare2:
                for i in range(spelare2.count(kort_val)):
                    spelare1.append(kort_val)
                    spelare2.remove(kort_val)
            else:
                random_kort = random.choice(kort)
                spelare1.append(random_kort)
                kort.remove(random_kort)
                print("Finns i sjön", "Du Fick", random_kort)
                break
        elif spelar_val == "3":
            if kort_val in  spelare3:
                for i in range(spelare3.count(kort_val)):
                    spelare1.append(kort_val)
                    spelare3.remove(kort_val)
            
            else:
                random_kort = random.choice(kort)
                spelare1.append(random_kort)
                kort.remove(random_kort)
                print("Finns i sjön", "Du Fick", random_kort)
                break

        else:
            print("Error")
            continue
    check_kort()
    while True:
        os.system("cls")
        if len(spelare2) == 0:
            random_kort = random.choice(kort)
            spelare1.append(random_kort)
            kort.remove(random_kort)

        print("Du har", spelare2poäng, "Par")
        print("Välj ett kort", spelare2)
        kort_val = input()
        print("välj en spelare")
        spelar_val = input()
    
        if kort_val not in spelare2:
            print("Du har inte detta kort")
            continue

        print("välj en spelare")
        spelar_val = input()

        if spelar_val == "1":
            if kort_val in spelare1:
                for i in range(spelare1.count(kort_val)):
                    spelare2.append(kort_val)
                    spelare1.remove(kort_val) 
            else:
                random_kort = random.choice(kort)
                spelare2.append(random_kort)
                kort.remove(random_kort)
                print("Finns i sjön", "Du Fick", random_kort)
                break     

        elif spelar_val == "3":
            if kort_val in  spelare3:
                for i in range(spelare3.count(kort_val)):
                    spelare2.append(kort_val)
                    spelare3.remove(kort_val) 
            else:
                random_kort = random.choice(kort)
                spelare2.append(random_kort)
                kort.remove(random_kort)
                print("Finns i sjön", "Du Fick", random_kort)
                break
        
        else:
            print("Error")
            continue
    check_kort()
    
    while True:
        os.system("cls")
        
        if len(spelare3) == 0:
            random_kort = random.choice(kort)
            spelare1.append(random_kort)
            kort.remove(random_kort)
        
        print("Duhar", spelare3poäng, "Par")
        print("Välj ett kort", spelare3)    
        kort_val = input()
        print("välj en spelare")
        spelar_val = input()
    
        if kort_val not in spelare3:
            print("Du har inte detta kort")
            continue

        print("välj en spelare")
        spelar_val = input()

        if spelar_val == "2":
            if kort_val in spelare2:
                for i in range(spelare2.count(kort_val)):
                    spelare3.append(kort_val)
                    spelare2.remove(kort_val) 
            else:
                random_kort = random.choice(kort)
                spelare3.append(random_kort)
                kort.remove(random_kort)
                print("Finns i sjön", "Du Fick", random_kort)
                break
                

        elif spelar_val == "1":
            if kort_val in  spelare1:
                for i in range(spelare1.count(kort_val)):
                    spelare3.append(kort_val)
                    spelare1.remove(kort_val)            
            else:
                random_kort = random.choice(kort)
                spelare3.append(random_kort)
                kort.remove(random_kort)
                print("Finns i sjön, du Fick", random_kort)
                break
        else:
            print("Error")
            continue
    check_kort()
    



