unit = input("enter the temperature in celcius or fahrenheit (c/f): ")
temp = float(input("enter the temperature"))

if  unit  == "c":
    temp = round((9*temp/5)+32 , 1)
    unit = "fahrenheit"
elif unit == "f":
    temp = round((temp - 32)*5/9 , 1)
    unit = "celcius"
else:
    print(f"the {unit} is invalid")


print(f"the new{temp} {unit}")