'''
    Cafe management system using python we using Dict and list for it.
    
'''
#create Dict for menu
food_prize={
    "pizza":100,
    "chicken":250,
    "coldcoffee":120,
    "naan":35,
    "mojito":60
}

#menu function for print the menu of all the items

def menu():
    print("\n WELCOME TO OUR RESTURANT SIR \n")
    print("Pizza- 100")
    print("Chicken- 250")
    print("Coldcoffee- 120")
    print("Naan- 35")
    print("Mojito- 60")
    
menu()


def order(food_prize): #Dict pass
   totalbill=[] #create a list for the total bill count
   while True:
      qus=input("Are you order something: ")
      if(qus=="yes"):
            orderitem=input("Which dish you want to order sir: ").lower()#we use lower method if user give capital letter in input.
            totalbill.append(food_prize[orderitem.lower()]) #appendmethod to append the food prize in to the list
      else: 
          print(f"Sir your total bill is {sum(totalbill)}") #atlast print the total bill 
          break #for terminate the loop
    
order(food_prize) #pass Dict to the function 