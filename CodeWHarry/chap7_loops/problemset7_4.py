n = int(input("enter the number :"))

for i in range (2,n):
    if(n % i):
        print("the number is not prime")
        break
else:
    print('the number is prime')