'''
Find the largest string which present in the list .
we have to find the maximum number of that string which is present in the list

'''

list=["biswajit","biswabhusana","nikhil","subhranshu"] #input some string 

checklist=[] # empty list for append the length of sub-strings

def append_lenofstr(list): #check the length of the string 
    for i in list:
        char_count=len(i)
        checklist.append(char_count) #append the length of the string in list
    check_max(checklist)  #check the maxmium value in the list we create new function for it.
    
def check_max(checklist):
    max_str=max(checklist) #max is used for find the maximum number of the list 
    print("\n") #for extra gap 
    print("longest length of string which is present in list: ",max_str)
    print("\n")
    
append_lenofstr(list)
    
print(checklist) #print the list
    
    
