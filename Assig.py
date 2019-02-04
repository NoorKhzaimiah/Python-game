
from random import randint
list=[]
Num= randint(0,100)
print("WELCOME !!! ")
print(" TO FIND THE TREASURE , YOU NEED TO SEARCH  .. GOOD LUCK ~ ")
Try = int(input('please enter your attempt number between 0 and 100:'))
list.append(Try)

if Try in range(Num+10,Num-10) :
           print("CLOSE!")
else:
        print("FARAWAY ! ")
print(list)
while Try!=Num :
    if Try > 100:
        print("OUT OF BOUNDS !!! ")

    elif Try < 1:
        print("OUT OF BOUNDS !!! ")

    Try=int(input("please enter your attempt number between 0 and 100:"))

    if (abs(Num-list[-1])<abs(Num-Try)):
      print("FARTHER!")
    else:
     print("CLOSER!")
    list.append(Try)

    print(list)
if Try==Num :
    print("SUCCESSFULL!!")
    print(f'The Number is :{Num}')
    print("YOUR TRYS : ")
    print(list)
