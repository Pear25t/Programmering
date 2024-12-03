ord = input ()

bokstäver = {}


for bokstav in ord:

    if bokstav in bokstäver:
        bokstäver[bokstav] += 1
    else:
        bokstäver[bokstav] = 1
    
        


print(bokstäver)