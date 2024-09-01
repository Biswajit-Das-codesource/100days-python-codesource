#Wap to find the Grade of your mark

def checkgrade(mark):
    if(mark>90):
        print("Your grade is A+ ")
        
    elif(mark>70 and mark<=90):
        print("Your grade is B")
        
    elif(mark>50 and mark<=70):
        print("Your grade is C")
        
    elif(mark>=40 and mark<=50):
        print("Your grade is C")
        
    else:  
        print("FAIL")
    
mark=int(input("Enter your mark: ")) #ENTER THE MARK

checkgrade(mark) #FUNCTION CALL 

