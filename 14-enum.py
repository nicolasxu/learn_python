# 14-enum

# https://docs.python.org/3/library/enum.html

from enum import Enum
class Color(Enum):
     RED = 1
     GREEN = 2
     BLUE = 3



print(Color.RED)
Color.RED


>>> print(repr(Color.RED))
<Color.RED: 1>


>>> type(Color.RED)
<enum 'Color'>
>>> isinstance(Color.GREEN, Color)
True
>>>

>>> print(Color.RED.name)
RED



class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3
for shake in Shake:
    print(shake)

"""
Shake.VANILLA
Shake.CHOCOLATE
Shake.COOKIES
Shake.MINT
"""


>>> Color(1)
<Color.RED: 1>
>>> Color(3)
<Color.BLUE: 3>

>>> Color['RED']
<Color.RED: 1>
>>> Color['GREEN']
<Color.GREEN: 2>


>>> member = Color.RED
>>> member.name
'RED'
>>> member.value
1