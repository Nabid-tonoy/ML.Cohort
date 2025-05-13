#TASK 2
CITIES=("Dhaka","New York","Tokyo","Shibuya","Toronto")
print(CITIES[2])
print("tuple to list convertion:")
New_CITIES=list(CITIES)
print(New_CITIES)
print("Adding new city-")
x=input(f"Add new city:",)
New_CITIES.append(x)
print(f"the new list is",New_CITIES)
print("list to tuple")
New_CITIES2=tuple(New_CITIES)      #convertion to tuple
print(f"So the tuple is:",New_CITIES2) #printing the modified tuple

    