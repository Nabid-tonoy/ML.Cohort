#for loop
fruits = ["apple","banana","jackfruit"]
for x in fruits:
    print(x)
#range
for x in range(1,11):
    print(x)
#reversed range
for x in reversed(range(1,11)):
    print(x)
print("Happy New year")
#range by gap in between multiple steps:
for x in range (1,11,2):
    print(x)
#for lopp with strings
credit_card= "1235-4567-2344-2134"
for x in credit_card:
    print(x)
#continue and break at for loop
##continue operation:
for x in range (1,23):
    if x==12:
        continue
    else:
         print(x) 
##break operation:
for x in range (1,23):
    if x==12:
        break
    else:
         print(x)
#organizing the numbers horizontally
for x in range(1,23):
    print(x,end=" ")
#show that (1 2 2 3 3 3 4 4 4 4) 
for i in range(1,5):
     for _ in range(i): #here _ used to Repeat the following block of code i times
         print(i,end= " ")