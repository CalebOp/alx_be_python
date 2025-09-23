num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation(+, -,*,/):")
addition = num1 + num2
subtract = num1 - num2 
multiply = num1 * num2
if num2 != 0:
    divide = num1 / num2 
else:
    divide = "Cannot divide by zero"
match operation:
    case "+":
        print ("The result is", addition)
match operation:
    case "-":
        print ("The result is", subtract)
match operation:
    case "*":
        print ("The result is", multiply)
match operation:
    case "/":
        if num2 !=0:
            print ("The result is", divide)
        else:
            print("Cannot divide by zero.")
match operation:
    case "+":
        print ("The result is", addition)
