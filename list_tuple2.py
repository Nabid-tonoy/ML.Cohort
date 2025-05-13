fruits= ["coconut","banana","orange","licchi" ] #number bad e onno kono word use korar somoy "" use korbo
print(fruits[0]) #access elements
print(fruits[0:3])#first 3 elemnts
print(fruits[::-1])#backward count
print(fruits[::2])#every 2nd element
#with loop
for fruit in fruits:
    print(fruit) #list e ja ja ase ta print korlam
#different classification of collecction
fruits= ["coconut","banana","orange","licchi" ]
print(dir(fruits))
print(help(fruits))#konta kmne ki kore janar jonno
#boolean way to find if that element is in list
print("apple" in fruits)    #false ba true show korbe
print("banana" in fruits)#........................
fruits= ["coconut","banana","orange","licchi" ]
#fruits.insert (2,"pineapple")# 2 use koray 2 ta pore pineapple add hoise 
#fruits.sort()
#fruits.clear
fruits.index ("coconut")
print(fruits)

#Set
fruits= {"coconut","banana","orange","licchi" } 
#set is unordered 
#tupple agertay ase