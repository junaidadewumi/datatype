#  Assignment
#  Write a program that will ask a user the following information;
#  firstName, lastName, location, value1, value2, then you are going to add the values the user supplies as value1 and value2 together
#  then print a statement having all the information the user supplied 
# i.e my full name is......, i am from ......, my total score is.....

# SOLUTION 
fn = input("Enter your first name: ")
ln = input("Enter your last name: ")
location = input("enter your location: ")
val1 = int(input("enter your first value: "))
val2 = int(input("enter your second value: "))
value = val1 + val2
# print(f"My name is {fn} {ln}, I am from {location}, my total score is {value}")  #this is format print type
print("my name is " + fn + " " + ln + ", " + "i am from " + location + ", " + "my total score is " + str(value)) #this is concatenation print type