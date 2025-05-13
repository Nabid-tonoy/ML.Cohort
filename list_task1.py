#task-1(lists)
Numbers=[] #creating a blank list,where we will add numbers
print("enter 5 numbers:" )
for x in range (5):
    num= float(input(f"number {x+1}:")) #x+1 use number 5 pornjonto anar jonno ,as range(5) is limited to 0-4
    Numbers.append(num)
print("the list of number is",Numbers)
print("Enter new number to add the list-") #adding new number
num_1=float(input(f"new number:"))
Numbers.append(num_1)
print("the new list is:",Numbers)
print("Removing the 2nd number") #removing
print("the second number is:",Numbers[1])
Numbers.remove(Numbers[1])
print("the new list is:",Numbers)
sum=Numbers[0]+Numbers[1]+Numbers[2]+Numbers[3]+Numbers[4] #summation
print(f"the sum of the numbers in the list is:",sum)
