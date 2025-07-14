n = int(input("enter thr number:"))
fact = 1
i = 1

while i<=n:
    fact = fact*i
    i+=1

print(f"the factorial of {n} is {fact}")