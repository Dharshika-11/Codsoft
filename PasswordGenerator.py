import random

uppercase_letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters= "abcdefghijklmnopqrstuvwxyz"
numbers= "0123456789"
symbols= "()[]{}@#$%^&*!;:/?.,="

upper,lower,nums,syms= True,True,True,True

all= ""

if upper:
    all+=uppercase_letters
if lower:
    all+=lowercase_letters
if nums:
    all+=numbers
if syms:
    all+=symbols
   
length= 10
amount= 14

for x in range(length):
    password= "".join(random.sample(all,length))
    print(password)
