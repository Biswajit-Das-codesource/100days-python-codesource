#FACTORIALOF THE NUMBER

#math module in python
# import math

# number=int(input("Enter the number: "))
# print(math.factorial(number))


#==================  OR  ========================


number=int(input("enter the number: "))
f=1
while(number>0):
    f=f*number
    number=number-1

print(f)