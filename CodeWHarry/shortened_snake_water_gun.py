import random

computer = random.choice([-1, 0, 1])
youstr = input('enter your choice:')
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}

you = youDict[youstr]

print(f'you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}')

if (computer==you):
    print("It's a draw")
    
else:
    '''
    if(computer == 1 and you == 0): 1
        print('you win!')
    elif(computer == 1 and you == -1): 2
        print("you lose!")
    elif(computer == -1 and you == 1): -2
        print("you win!")
    elif(computer == -1 and you == 0): -1
        print("you lose!")
    elif(computer == 0 and you == -1): 1
        print("you win!")
    elif(computer == 0 and you == 1): -1
        print("you lose!")
    else :
        print("something went wrong!")
        '''
    
    if((computer-you == 2) or (computer-you == -1)):
        print("you lose!")
    else:
        print("you win!")
    
              
        

    
    
    

