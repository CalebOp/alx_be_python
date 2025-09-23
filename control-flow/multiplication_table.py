number = int(input("Enter a number to see its multiplication table:"))
for x in range(1,11):
    table = number * x
    print(number,"*", x, "=", table)