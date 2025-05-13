#list data=[12,34,55,567] list dekhte emn
data=[12,34,55,567]
data.append (233) #add numbers to the list
data.remove (34)  #removes numbers from the list
print (data)
#tuple data=(12,34,55,567) tuple dekhte emn
data = (12,34,55,567) # we cant change or modify in tuple 
#but we can convert tuple into list
#convertion
data= (12,34,55,567)
new_data=list(data) #converted in to list
new_data.append (233) 
new_data.remove (34)  
print (new_data)