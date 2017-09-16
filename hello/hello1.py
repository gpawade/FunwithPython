

#print message
print( "hello world! first sample")

# string formating

print( "# string formating")
name = "John"
print( "Hello, %s!" % name)

age =32
print( "%s is %d year old" % (name, age))


# LIST

print( "#List example")

mylist = []
mylist.append("one")
mylist.append(12);

intVal = mylist[1];

for item in mylist:
	print( item);


mylist2 = [1,2,3]
for item in mylist2:
	print( item);




# conditional loop

x=1
if x==1:
	print( "x is 1")