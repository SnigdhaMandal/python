weight = float(input("enter your weight:"))
unit = input("kilograms or pounds (k/l):")

if unit == "k" :   
    weight = weight*2.205
    unit = "Lbs "
elif unit == "l":
    weight = weight/2.205
    unit = "Kgs"
else:
    print(f"{unit} is invalid")

print(f"your new weight is: {weight}{unit}")

