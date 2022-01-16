firstNumber = int(input("Enter the first number: "))
operator = input("Enter an operator: ")
secondNumber = int(input("Enter the second number: "))

result = 0

if operator == "+":
    result = firstNumber + secondNumber
    print(result)
elif operator == "-":
    result = firstNumber - secondNumber
    print(result)
elif operator == "*":
    result = firstNumber * secondNumber
    print(result)
else:
    result = firstNumber / secondNumber
    print(result)