#Problem2
#writing programm that would prompt the username in the format Domain Name-Username.

print("#######################################")
print("WELCOME TO DBS CONSOLE")
print("#######################################")

#asking the user to input his credentials

student=input("enter username")
index= student.index("\\") #preparing an index
student_id=student[:index]
student_name= student[index:][1:]

#printing the result as the seprate combination
print("Domain",student_id)
print("Username",student_name)

