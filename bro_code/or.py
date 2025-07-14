temp = int(input("enter the temperatue:"))
is_raining = True
if temp < 0 or temp > 35 or is_raining:
    print("game cancel")
else:
    print("game is on")