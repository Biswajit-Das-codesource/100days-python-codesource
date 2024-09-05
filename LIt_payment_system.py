database={}

while True:
    print("====\n WELCOME TO LIT PAYMENT APP==== \n")
    print("1.Create New Bank Account ")
    print("2.add money")
    print("3.withdraw money")
    print("4.For Lit Fee payment")
    print("5.check balance")
    print("6.See your bank details")
    print("7.EXIT")
    
    choice=int(input("Enter your choice: "))
    
    if(choice==1):
        print("\n ~~~~~~~ WELCOME TO BANK SECTION ~~~~~~ \n")
        print("\nState bank of india")
        print("Punjab national bank")
        print("Axis bank")
        print("HDFC bank \n")
        
        
        new_bank=input("Inwhich bank you want to open your account: ")
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        number=int(input("Enter your phone number: "))
        gender=input("Enter your gender: ")
        email=input("Enter your email address: ")
        set_cvv=int(input("Enter your Cvv: "))
        
        database[name]={new_bank,age,number,gender,email,set_cvv}
        
        print("\n YOUR BANK ACCOUNT HAS BEEN CREATED SUCCESSFULLY \n")
        
        
        
    elif(choice==2):
       money=0
       print(database)
       username=input("please enter account holder name: ")
       if(username in database):
           amount=int(input("enter the amount you want to add in your bank account: "))
           money=money+amount
       else:
           print("SORRY!! WE CAN'T FOUND YOUR ACCOUNT")
           
    elif(choice==3):
        print("\n ======WELCOME TO WITHDRAW SECTION ========= \n")
        receiver_name=input("please enter your name sir: ")
        
        if(receiver_name in database):
            receive_money=int(input("Enter the amount"))
            if(receive_money>money):
                print("Sorry you have that much money")
            else:
                amount=amount-receive_money
                print(f"money has been withdrawn of rupees{receive_money}")
                print(f"Now you have {amount} of money ")
        else:
            print("Soorry we cant find your information ")
            
    elif(choice==4):
        print("\n=====WELCOME TO LITINDIA PAYEMENT APP====\n")
        student_name=input("Enter your name: ")
        payment_pay=int(input("Enter your amount: "))
        if(payment_pay>money):
            print("Soory you have not that much money")
        else:
            money=money-payment_pay
            print("PAYMENT successfully")
      
    elif(choice==5):
        print("====CHECK BALANCE====")
        name=input("Enter your name: ")
        print(f"{name}sir you have {money}")
    
    elif(choice==6):
        name=input("'Enter your name: ")
        if name in database:
            print(database)
    
    elif(choice==7):
        break
    else:
        print("sorry please enter the correct option")
           
        
        
        
        
        
    