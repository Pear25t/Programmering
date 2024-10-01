x = ["a", "o" ,"i", "u" ,"å", "e", "y" ,"ä" ,"ö"]
ordet = input()
antal_x = 0
for bokstav in ordet:
    if bokstav in x:
        antal_x += 1
        
        
print (ordet, "har", antal_x)