# Exercise 2 Template

# Do not modify the file name or function header

# Adds e to mylist and returns the resulting list
def list_add(mylist, e):
	mylist.append(e)
	return(mylist)

# Removes the first occurrence of e in mylist and returns the resulting list 
def list_del(mylist, e):
	mylist.remove(e)
	return(mylist)
# Adds the tuple t (value, key) to mydict and returns the resulting dictionary
def dict_add(mydict, t):
	mydict[t[0]]=t[1]
	return(mydict)