#Wap to find the word which is present in the poem.txt or not 

#If it is present then print "FIND" otherwise "NOT FIND"

userchoie=input("enter the word to search in poem txt file:  ")

str=open("poem.txt")  #bydefault the file is in read mode
data=str.read()    #read method
if(userchoie in data):   #check present or not
    print("yess!!  avaliable")
else:
    print("not avaliable")
print(data)
str.close()