numbers = [1, 2, 99, 62, 19, 92, 76, 82281, -31, -4]

odd_numbers = []
even_numbers = []

for number in numbers:
    if number%2 == 0:
        even_numbers.append (number)
    else:
        odd_numbers.append (number)



print (even_numbers)
print (odd_numbers)