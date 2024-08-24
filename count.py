#WAP TO PROGRAM TO COUNT THE NUMBER OF ALBHABETS AND NUMBER OF DIGIT IN THE STRING 

str="biswajit das-000072762864"
stringcount=0
numbercount=0
for i in str:
    if(i.isalpha()):
        stringcount+=1
    elif(i.isalnum()):
        numbercount+=1

print("number of string :",stringcount)
print("number of number:",numbercount)