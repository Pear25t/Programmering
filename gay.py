ord = input()
vänd = ""

for i in reversed(ord):
    print(i)
    vänd += i


if ord == vänd:
    print("good job")
else:
    print("gay")
