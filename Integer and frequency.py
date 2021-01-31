#Problem3
#Asking the user to promt number of integers. 

print("###################################")
print("WELCOME TO DBS CONSOLE")
print("###################################")
 
Elementlist= [] 
  
 
number = int(input("Input the number of elements to be stored in the list : ")) 
print("Input", number ," elements in the list:")  
 
for i in range(0, number): 
    element = int(input ("Element-") ()) 
  
    Elementlist.append(element)  
      
print("The frequency of all elements in the list") 


frequency = {}
for item in Elementlist:
   if (item in frequency):
      frequency[item] += 1
   else:
      frequency[item] = 1
for key, value in frequency.items():
   print("% s occurs % d times" % (key, value))



