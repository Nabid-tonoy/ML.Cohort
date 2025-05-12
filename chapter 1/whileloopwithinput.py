#while with user input
name=input("enter your name:")
while name=="":#when empy string(means no name has been written)
    print("there is no name!") #(then print this)
    name=input("enter your name:") #breaking that loop we again asking for their name
print(f"hello {name}!")
#age count (using logic)
age=int(input("Enter your age:"))
while age<0 :
    print("Age cant be negative !")
    age=int(input("Enter your age:"))
    print(f"u r {age} years old")  
#age count with logic op
age=int(input("Enter your age:"))
while age<0 or age>200:
    print("Age cant be negative or too !")
    age=int(input("Enter your age:"))
    print(f"u r {age} years old")
#loop with specific key to quit
food=input("Enter the food u like(q to quit):")
while not food=="q" :
    print(f"you like {food}")
    food=input("Enter another food u like:")
print("bye")
