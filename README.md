# Fun with python

- comment start with `#` in python


## Variable / Datatype

### int
		myInt = 2

### float
		myFloat = 7.0
		myFloat = float(7)



### List

	mylist = []
	mylist.append(1)
	mylist.append(2)
	mylist.append(3)
	myList[-1] = 3.5 		# this refere last item

OR

	mylist = [1, 2, 3]

	print(mylist[0]) # prints 1
	print(mylist[1]) # prints 2
	print(mylist[2]) # prints 3

	# prints out 1,2,3
		for x in mylist:
    		print x

	#slicing:
		thelist[1:3] 
 		thelist[2:] 

 	len(thelist)     # length


- ! Tuples are fixed size in nature whereas lists are dynamic.
- ! In other words, a tuple is immutable whereas a list is mutable.

### Dictionary

	mydist = { "key1" : "value1"}
	mydist["key1"]

	creation: 
		emptyDict = {}
	 	thisdict = {‘a’:1, ‘b’:23, ‘c’:”eggs”}
	accessing: 
		thisdict[‘a’]   #returns 1
		deleting: del thisdict[‘b’]
	finding: 
		thisdict.has_key(‘e’) 		#returns False
	 	thisdict.keys() 			#returns [‘a’, ‘c’]
	 	thisdict.items() 			#returns [(‘a’, 1), (‘c’, ‘eggs’)]
	 	‘c’ in thisdict 				#returns True
	 


### Set
 A set is unordered collection with no duplicate element
e.g
	basket = ['one', 'two', 'one', 'three', 'two']
	elm = set(basket)             #create a set without duplicate

### Tuples
A tuple consists of a number of values separated by commas. They are useful for ordered pairs and returning several
values from a function.

creation: 

	emptyTuple = ()
	singleItemTuple = (“spam”,) note the comma!
	thistuple = 12, 89, ‘a’
	thistuple = (12, 89, ‘a’)

accessing: 
	
	thistuple[0] returns 12



### String formating

	name = "john"
	print "Hello %s" % name






## Condition

### if:
 
	 if test:
	 	#do stuff if test is true
	 elif test 2:
	 	#do stuff if test2 is true
	 else:
	 	#do stuff if both tests are false

### while:

	 while test:
	 	#keep doing stuff until
	 	#test is false

### for:

	 for x in aSequence:
	 	#do stuff for each member of aSequence
	 	#for example, each item in a list, each
	 	#character in a string, etc.

	 for x in range(10):
	 	#do stuff 10 times (0 through 9)

	 for x in range(5,10):
	 	#do stuff 5 times (5 through 9)



##### enumerate()
 position index & corresponding value can be retrieve at the same time using enumerate() method.

		for i, v in enumerate(['tic', 'tac', 'toe']):             
			print i
			print v

##### zip()
to loop over two or more sequence at same time, then user zip() method	

		questions = ['name', 'quest', 'favorite color']
		answers = ['lancelot', 'the holy grail', 'blue']
		for q, a in zip(questions, answers):
			print 'What is your {0}?  It is {1}.'.format(q, a)

			#output - What is your name?  It is lancelot.

##### reverse()
 to loop over sequence in reverse

		for i in reversed(xrange(1,10,2)):
			print i

##### sorted()
loop over sequence in sorted order


##### iteritems()
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the iteritems() method



***

## File

open:
	
	thisfile = open(“datadirectory/file.txt”)   # note: forward slash, unlike Windows! This function

Note - defaults to read-only. Option - `r` - read only, `w` - writing, `a` - appending

accessing:
	
	thisfile.read() 			# reads entire file into one string
	thisfile.readline() 		# reads one line of a file
	thisfile.readlines() 		# reads entire file into a list of strings, one per line
	for eachline in thisfile:  	# steps through lines in a file


`write()` : This method writes a sequence of strings to the file.

	write ()			# Used to write a fixed sequence of characters to a file
	writelines()		# writelines can write a list of strings.

`close()` : When you’re done with a file, use close() to close it and free up any system
resources taken up by the open file

	file.close()

Example : 

	filename = "hello.txt"
	file = open(filename, "r")
	
	# To read one line at a time, use:
	print file.readline()

	# To read a list of lines use:
	print file.readlines()

	# read line by line
	for line in file:
	   print line,

	# write to file
	file.write("Hello World")
	file.close()

	# write multiple lines to file
	lines_of_text = ["a line of text", "another line of text", "a third line"]
	file.writelines(lines_of_text)
	
	# close file
	file.close()


