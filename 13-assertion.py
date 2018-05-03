13-assertion

"""
When it encounters an assert statement, Python evaluates the accompanying expression, 
which is hopefully true. If the expression is false, 
Python raises an AssertionError exception.

assert Expression[, Arguments]
"""

#!/usr/bin/python

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
print KelvinToFahrenheit(-5)


"""
32.0
451
Traceback (most recent call last):
   File "test.py", line 9, in <module>
      print KelvinToFahrenheit(-5)
   File "test.py", line 4, in KelvinToFahrenheit
      assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
"""
