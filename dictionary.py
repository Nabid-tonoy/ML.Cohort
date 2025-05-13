capitals= {"bangladesh":"Dhaka",
           "India": "new delhi",
           "uganda" : "Nigeria"}
print (capitals.get("bangladesh"))
print (capitals.get("India"))

#with if else
capitals= {"bangladesh":"Dhaka",
           "India": "new delhi",
           "uganda" : "Nigeria"}
if capitals.get("India"):
   print("that capital does exist")
else:
   print("that capital doesnt exist")

#update our dictionary 
capitals.update({"germany":"berlin"})  #update korlam amar capitals er element
print(capitals)
#remove
capitals.pop("india")
print(capitals)
#keys method
keys = capitals.keys()
for key in capitals.keys():
    print(key)

#values method
values=capitals.values() #values method capitals er moddhe ja ase oigulake list e convert kore
print(values)
#items method
items=capitals.itemn()
for key,value in capitals.item():
    print(f"{key}:{value}")
