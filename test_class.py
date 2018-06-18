class A(object):
	def __new__(cls):
		print ("A.__new__ is called") # this is never called
		return super(A, cls).__new__(cls)
	def __init__(self):
		self.hello = "world"
		print("hello in __init__ ")



aInst = A()