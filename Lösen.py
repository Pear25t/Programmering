import random

alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
siffror = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
täcken = ["!", "#", "@", "£", ",", ";", ".", ":", "¤", "$", ">", "<", "%", "&", "/", "{", "}", "=", "(", ")", "+", "?"]
lösen = []

print("Hur långt ska lösenenordet vara?")
längd = int(input())

print("Stora bokstäver?")
big = input()
if big == "ja":
    big = True
else:
    big = False

print("Vill du det ska innehålla siffror?")
numer = input()
if numer == "ja":
    numer = True
else:
    numer = False

print("Ska det innehålla speciall tecken?")
speciall = input()
if speciall == "ja":
    speciall = True
else:
    speciall = False

while len(lösen) < längd:
    randomize = random.randint(0,9)
    if(randomize >= 0 and randomize <= 6):
        random_bokstav = random.choice(alfabet)
        if (big):
            if(random.randint(0,1) == 1):
                random_bokstav = random_bokstav.upper()
        lösen.append(random_bokstav)
        
    elif(randomize >= 7 and randomize <= 8):
        if (numer):
            random_siffra = random.choice(siffror)
            lösen.append(random_siffra)
            

    elif(randomize ==9):
        if (speciall):
            random_täcken = random.choice(täcken)
            lösen.append(random_täcken)


print(lösen)