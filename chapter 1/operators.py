#operator (task 1)
x=float(input("Type the 1st number(x):"))
y=float(input("Type the 2nd number(y):"))
z=float(input("Type the 3rd number(z):"))
if x>y and x>z:
    print("x is largest")
elif y>x and y>z:
    print("y is largest")
else:
    print("z is largest")
#operator (task 2)
x=float(input("input your cg (person 1):"))
y=float(input("input your cg (person 2):"))
z=float(input("input your cg (person 3):"))
avg_CG=(x+y+z)/3
if x<y and x<z:
    print("person 1 has the lowest CG")
elif y<x and y<z:
    print("person 2 has the lowest CG")
else:
    print("person 3 has the lowest CG")
print("Gathered CG's are :" + str(x)+" "+str(y)+" "+str(z) )
print("The avg cg is:"+ str(avg_CG))

