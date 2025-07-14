operator = input("enter the operator(- + *  % ):")
num1 = int(input("enter the number:"))
num2 = int(input("enter the number:"))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator  == "-":
    result = num1 - num2
    print(round(result,3))
elif operator  == "*":
    result = num1 * num2
    print(round(result,3))
elif operator  == "%":
    result = num1 % num2
    print(round(result,3))
else:
    print(f"{operator} is not valid")