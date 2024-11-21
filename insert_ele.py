'''
 Wap to give the mutiple element at one run using looping & append it into a list
 and print only even numbers from that list
'''

#enter the number of element to insert 

num=int(input("Enter the number of insert element: "))
list=[]

for i in range(1,num+1):
    
    element=int(input(f"Enter the {i} number: "))
    #we use fstring for better input field
    
    if(element%2==0): #check the even numbers
        list.append(element)
    else:
        print("")
        
print(list)

    