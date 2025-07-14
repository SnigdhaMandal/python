marks1 = int(input("enter the marks1 :"))
marks2 = int(input("enter the marks2 :"))
marks3 = int(input("enter the marks3 :"))
total_percentage = ((marks1+marks2+marks3)*100)/300
if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33) :
    print('congo! you passed')
    
else:
    print('sorry! you failed')

print('the percentage is',total_percentage)