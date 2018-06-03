19-lambda

In Python, anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.

lambda arguments: expression


# Program to show the use of lambda functions

double = lambda x: x * 2

# Output: 10
print(double(5))

####################################
# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)