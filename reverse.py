#WAP TO REVERSE THE NUMBER BY THR USERS AND CHECK WHETHER THE ORIGINAL AND REVERSE NUMBERS ARE EQUAL OT NOT


def reverse(num):
    s=0
    originalnumber=num
    while(num>0):
        r=num%10
        s=s*10+r
        num=num//10
    #check it is same ot not
    reversenum=s
    if reversenum==originalnumber:
        print("yes!! it is same as reverse number")
    else:
        print("NO!!! it is not same as reversed number")
        
#input and function call 
num=int(input("Enter the number"))
reverse(num)
        


