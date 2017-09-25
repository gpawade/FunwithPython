# class defination
class Person():
	"""my first test class"""
	def __init__(self, first, last):
		self.first = first;
		self.last  = last;


# create the instance
obj = Person("john", "doe");

print(obj.first);
print(obj.last);