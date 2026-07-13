 #1. if else
a = int(input('enter number A='))
b = int(input('emnter number B='))
if( a > b):
    print("A gratenthan B")
else:
    print('B gratenthank A')    



 #2.if elif

per = float(input('Enter percantage = '))
if(per < 35 ):
       print('fail')
elif(per >= 35 and per <=60):
     print('c garde')

elif(per >= 61 and per <=70):
     print('b garde')
elif(per >=71 and per <=80):
     print('grade A')
elif(per >=81 and per <= 100):
     print('A+ grade')
else:
     print('invalid number')               


#3. nasted if
man =int(input('enter you age = '))
if(man > 18):
     
     if(man <= 60):
          print('valid ')
     else:
         print('not valid')
else:
     print('not valid')

#4. match
print('1.English 2.Hindi 3.Gujrati')
choice = int(input('Enetr your choice'))
match choice:
     case 1 :
          print('you selected English')
     case 2 :
          print('you selected Hindi')
     case 3 :
          print ('you slected Gujrati')    
     case _:
          print('invalid choice')