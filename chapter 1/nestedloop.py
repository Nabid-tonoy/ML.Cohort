#nested for loop
for x in range(3):
    for y in range(1,12):
       print(y,end=" ")
    print()
#project(with user input)
rows=int(input("enter the number of rows:"))
columns=int(input("enter the number of columns:"))
symbol=input("enter the symbol:")
for x in range(rows):
    for y in range(columns):
       print(symbol,end=" ")
    print()
