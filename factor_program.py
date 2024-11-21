#Find the factor of the number and print it in to a list

number=int(input("Enter the number: "))

list=[]
for i in range(1,number+1):
   if(number%i==0):
       list.append(i) #We use append method to add the element into the list
   
print(list)
