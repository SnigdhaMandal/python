p1 = 'make a lot of money'
p2 = 'buy now'
p3 = 'subcribe this'
p4 = 'click this'

message = input ("enter the message:")

if ( p1 in message or p2 in message or p3 in message or p4 in message):
    print('it is a spam message')
else :
    print("it is not a spam message")