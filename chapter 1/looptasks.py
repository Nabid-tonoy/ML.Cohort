# show that (** ** ** ** )
symbol= "**"
for row in range(1):
    for column in range(4):
        print(symbol,end=" ") 
#show that (** * **)
symbol= "** * **"
for row in range(1):
    for column in range(1):
        print(symbol,end=" ")
#show that (1 2 2 3 3 3 3 4 4 4 4 4)
number=1
number_2=2
number_3=3
number_4=4
for i in range (1):
    for j in range (1):
       print(number,end=" ")
for  i in range (1):
    for j in range (2):
       print(number_2,end=" ")      
for  i in range (1):
    for j in range (4):
       print(number_3,end=" ") 
for  i in range (1):
    for j in range (5):
       print(number_4,end=" ")    
