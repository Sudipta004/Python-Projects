import random
import time
k=input("Press enter to begin")
print('='*30)
print("Think of a number 1 to 50")
k=input("Press enter once done")
print('='*20)
print("Double the number you thought of")
n=random.randrange(30,101,10)
print("1 - Add",n,"to it \n------------------------------\n2 - Half the number \n------------------------------\n3 - Deduct the number you thought of")
print('='*30)
k=input(" Press enter once done")
print("Processing")
for i in range(5):
    print(".")
    time.sleep(1)
print("You got ",n//2)
a=input("Press ENTER to close")