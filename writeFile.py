#Write in to the File 

str="my name is biswajit das"
f=open("fil1.txt","w") 

f.write(str)

print("successfully append in file")

f.close()

#.close() is compulsory if you open that file