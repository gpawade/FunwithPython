# Fun with python


- comment start with # in python


### Variable 

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


- ! Tuples are fixed size in nature whereas lists are dynamic.
- ! In other words, a tuple is immutable whereas a list is mutable.

### Dictionary

	mydist = { "key1" : "value1"}
	mydist["key1"]

### Set
 A set is unordered collection with no duplicate element
e.g
	basket = ['one', 'two', 'one', 'three', 'two']
	elm = set(basket)             #create a set without duplicate


### String formating

	name = "john"
	print "Hello %s" % name

### Looping

- ### enumerate()
 position index & corresponding value can be retrieve at the same time using enumerate() method.
		for i, v in enumerate(['tic', 'tac', 'toe']):             
			print i
			print v
- ### zip()
to loop over two or more sequence at same time, then user zip() method	

		questions = ['name', 'quest', 'favorite color']
		answers = ['lancelot', 'the holy grail', 'blue']
		for q, a in zip(questions, answers):
			print 'What is your {0}?  It is {1}.'.format(q, a)

			#output - What is your name?  It is lancelot.

- ### reverse()
 to loop over sequence in reverse
		for i in reversed(xrange(1,10,2)):
			print i

- ### sorted()
loop over sequence in sorted order


- ### iteritems()
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the iteritems() method