# 25. diff between tuple and list.py


str = "A tuple is a sequence of immutable Python objects. Tuples are sequences, \
	just like lists. The differences between tuples and lists are, the tuples cannot \
	be changed unlike lists and tuples use parentheses, whereas lists use square \
	brackets. Creating a tuple is as simple as putting different comma-separated values."


tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";

tup1 = ();
# To write a tuple containing a single value you have to include a comma, even though there is only one value −

tup1 = (50,);

# accessing value in tuple
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];


# Updating Tuples
no_update_ = "Tuples are immutable which means you cannot update or change the values \
	of tuple elements. You are able to take portions of existing tuples to create new \
	tuples as the following example demonstrates −"

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3;
(12, 34.56, 'abc', 'xyz')


tup = ('physics', 'chemistry', 1997, 2000);
print tup;
del tup;
print "After deleting tup : ";
print tup;
'''
('physics', 'chemistry', 1997, 2000)
After deleting tup :
Traceback (most recent call last):
   File "test.py", line 9, in <module>
      print tup;
NameError: name 'tup' is not defined
'''



# Basic Tuples Operations


len((1, 2, 3))	                            3	                            Length
(1, 2, 3) + (4, 5, 6)	                    (1, 2, 3, 4, 5, 6)	            Concatenation
('Hi!',) * 4	                            ('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
3 in (1, 2, 3)	                            True	                        Membership
for x in (1, 2, 3): print x,	            1 2 3	                        Iteration


# Indexing, Slicing, and Matrixes
L = ('Spam', 'SPAM!')
L[2]	'SPAM!'	Offsets start at zero
L[-2]	'Spam'	Negative: count from the right
L[1:]	('SPAM!', )	Slicing fetches sections


# No Enclosing Delimiters
'''
Any set of multiple objects, comma-separated, written without identifying symbols,
i.e., brackets for lists, parentheses for tuples, etc., default
to tuples, as indicated in these short examples −

'''

print 'abc', -4.24e93, 18+6.6j, 'xyz';
x, y = 1, 2;
print "Value of x , y : ", x,y;
'''
abc -4.24e+93 (18+6.6j) xyz
Value of x , y : 1 2

'''

# Built-in Tuple Functions
#1
cmp(tuple1, tuple2)
#Compares elements of both tuples.

#2
len(tuple)
#Gives the total length of the tuple.

#3
max(tuple)
#Returns item from the tuple with max value.

#4
min(tuple)
#Returns item from the tuple with min value.

#5
tuple(seq)
#Converts a list into tuple.