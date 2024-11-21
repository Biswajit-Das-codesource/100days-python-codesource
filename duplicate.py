'''
    find the duplicate letter in word 
    
'''
sentence=input("Enter the sentence:  ")

splitSen=sentence.split()
addsen=[]

for i in sentence:
    if(i not in addsen):
        addsen.append(i)
        
print(addsen)
str=" ".join(addsen)
print(str)