__init__.py 

# https://stackoverflow.com/questions/448271/what-is-init-py-for

# What goes in __init__.py?

"""
However you can import File into your __init__.py to make it available at the package level 
for other python file to import:
"""
# in your __init__.py
from file import File

# now import File from package
from package import File

Another thing to do is at the package level make subpackages/modules available with the __all__ variable. When the interpeter sees an __all__ variable defined in an __init__.py it imports the modules listed in the __all__ variable when you do:
"""
from package import *

"""