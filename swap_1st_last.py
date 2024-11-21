#Swap fist and last element in the list

def swap(list):
   size=len(list)
   temp=list[0]
   list[0]=list[size-1]
   list[size-1]=temp
   return list

list=[1,2,3,4,5,6,6]
print(swap(list))