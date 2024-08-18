def bank_details():
    print("1.State bank of india...")
    print("2.HDFC bank of india...")
    print("3.Punjab bank of india...")
    
    
def statebank():
    print("=====WELCOME TO STATE BANK OF INDIA=====")
    total_balance=0
    print("1.ADD MONEY")
    print("2.SEND MONEY")
    print("3.CHECK BANK BALANCE")
    print("4.EXIT")
    money=int(input("enter the choice"))
    while money!=4:
     
     if(money==1):
        receive=int(input("enter the add money:  "))
        total_balance=total_balance+receive
        print("your money is added succesfully.....")
        money=int(input("enter the choice"))
     elif(money==2):
        send=int(input("enter the send money:  "))
        total_balance=total_balance-send
        money=int(input("enter the choice"))
     elif(money==3):
        print(total_balance)
        money=int(input("enter the choice"))
    print("EXIT")


def HDFC_bank():
    print("=====WELCOME TO STATE BANK OF INDIA=====")
    total_balance=0
    print("1.ADD MONEY")
    print("2.SEND MONEY")
    print("3.CHECK BANK BALANCE")
    print("4.EXIT")
    money=int(input("enter the choice"))
    while money!=4:
     
     if(money==1):
        receive=int(input("enter the add money:  "))
        total_balance=total_balance+receive
        print("your money is added succesfully.....")
        money=int(input("enter the choice"))
     elif(money==2):
        send=int(input("enter the send money:  "))
        total_balance=total_balance-send
        money=int(input("enter the choice"))
     elif(money==3):
        print(total_balance)
        money=int(input("enter the choice"))
    print("EXIT")
    
    
def punja_bbank():
    print("=====WELCOME TO STATE BANK OF INDIA=====")
    total_balance=0
    print("1.ADD MONEY")
    print("2.SEND MONEY")
    print("3.CHECK BANK BALANCE")
    print("4.EXIT")
    money=int(input("enter the choice"))
    while money!=4:
     
     if(money==1):
        receive=int(input("enter the add money:  "))
        total_balance=total_balance+receive
        print("your money is added succesfully.....")
        money=int(input("enter the choice"))
     elif(money==2):
        send=int(input("enter the send money:  "))
        total_balance=total_balance-send
        money=int(input("enter the choice"))
     elif(money==3):
        print(total_balance)
        money=int(input("enter the choice"))
    print("EXIT")
    
    

bank_details()
choice=int(input("enter bank choice....."))
if(choice==1):
    statebank()
elif(choice==2):
    HDFC_bank()
else:
    punja_bbank()
    
    
        
    