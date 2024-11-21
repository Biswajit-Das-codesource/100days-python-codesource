'''
    Create a contact app which have the fecture of create ,view, update,delete,search,count 
    
    here we use membership & if-elif-else for this program    
'''

contact={}
while True:
    print("===Welcome to contact app===")
    print("1.Create contact app")
    print("2.View contact")
    print("3.update contact")
    print("4.delete contact")
    print("5.search contact")
    print("6.count contact")  
    print("7.Exit") 
    
    choice=int(input("Enter your choice: "))
    
    if(choice==1):
        name=input("Enter the person's name: ")
        if(name in contact):
            print("\nit's avaliable in the list\n")
        else:
            number=int(input("Enter the contact number : "))
            age=int(input("Enter the person age: "))
            email=input("Enter the email of the person: ")
            contact[name]={f"number:{number} , age: {age} , email: {email}"}
            print("CONTACT NUMBER WILL BE CREATED ")
    
    elif(choice==2):
        print("\n====WELCOME TO THE CONTACT SECTION====\n")
        print(contact)
        
    elif(choice==3):
        print("update section")
        print(contact)
        check_name=input("which number you want to update: ")
        if(check_name in contact):
            newcontact=input("enter the your new name: ")
            new_phone=int(input("Enter the new number: "))
            new_age=int(input("enter the new age: "))
            new_email=input("enter the new gamil: ")
            contact[newcontact]={f"newnumber: {new_phone},newage: {new_age} ,newemail: {new_email}"}
            print("\n new contact updated \n")
        else:
            print(f"THERE IS NO CONATACT LIKE {check_name}")
            
    elif(choice==4):
        print(contact)
        delete_contact=input("which contact you want to delete: ")
        if(delete_contact in contact):
            del contact[delete_contact]
            print("contact has been deleted")
        else:
            print("there is no contact like that ")
            
    elif(choice==5):
        search_contact=input("Enter the contact we want to search:  ")
        
        if(search_contact in contact):
            print(f"yes it is avaliable in contact {contact[search_contact]}")
        else:
            print("NOT found")
            
    elif(choice==6):
        print(f"Total number of contact is {len(contact)}")
        
    elif(choice==7):
        break
    else:
        print("PLEASE SELECT THE CORRECT CHOICE ")
        continue
    
        