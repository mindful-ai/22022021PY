Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # --------------------- datetime
>>> 
>>> from datetime import datetime
>>> 
>>> t = datetime.now()
>>> t
datetime.datetime(2021, 2, 24, 16, 54, 31, 257712)
>>> t.year
2021
>>> t.month
2
>>> t.day
24
>>> t.hour
16
>>> t.today
<built-in method today of type object at 0x00007FF8810BD6C0>
>>> t.minutes
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t.minutes
AttributeError: 'datetime.datetime' object has no attribute 'minutes'
>>> t.minute
54
>>> t.second
31
>>> # Wednesday, 24 February 2021, 4:54 PM"
>>> 
>>> f = "%A, %d %B %Y, %I:%M %p"
>>> t
datetime.datetime(2021, 2, 24, 16, 54, 31, 257712)
>>> t.strftime(f)
'Wednesday, 24 February 2021, 04:54 PM'
>>> t1 = datetime.now()
>>> t
datetime.datetime(2021, 2, 24, 16, 54, 31, 257712)
>>> t1
datetime.datetime(2021, 2, 24, 17, 0, 45, 399369)
>>> t1 - t
datetime.timedelta(seconds=374, microseconds=141657)
>>> 
>>> 
>>> # --------------------------------- itertools
>>> 
>>> from itertools import permutations, combinations
>>> 
>>> s = "ABCD"
>>> permutations(s)
<itertools.permutations object at 0x0000028FF3E0DE60>
>>> list(permutations(s))
[('A', 'B', 'C', 'D'), ('A', 'B', 'D', 'C'), ('A', 'C', 'B', 'D'), ('A', 'C', 'D', 'B'), ('A', 'D', 'B', 'C'), ('A', 'D', 'C', 'B'), ('B', 'A', 'C', 'D'), ('B', 'A', 'D', 'C'), ('B', 'C', 'A', 'D'), ('B', 'C', 'D', 'A'), ('B', 'D', 'A', 'C'), ('B', 'D', 'C', 'A'), ('C', 'A', 'B', 'D'), ('C', 'A', 'D', 'B'), ('C', 'B', 'A', 'D'), ('C', 'B', 'D', 'A'), ('C', 'D', 'A', 'B'), ('C', 'D', 'B', 'A'), ('D', 'A', 'B', 'C'), ('D', 'A', 'C', 'B'), ('D', 'B', 'A', 'C'), ('D', 'B', 'C', 'A'), ('D', 'C', 'A', 'B'), ('D', 'C', 'B', 'A')]
>>> list(permutations(s, 3))
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
>>> list(combinations(s))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list(combinations(s))
TypeError: combinations() missing required argument 'r' (pos 2)
>>> list(combinations(s, 4))
[('A', 'B', 'C', 'D')]
>>> 
>>> 
>>> # ----------------------------------- functools
>>> 
>>> from functools import reduce
>>> L = [1, 2, 3, 4, 5]
>>> reduce(lambda x, y: x + y, L)
15
>>> # ------------------------------------ collections
>>> 
>>> from collections import Counter
>>> L = ["red", "red", "yellow", "green", "yellow", "red"]
>>> 
>>> D = []
>>> D = {}
>>> for word in L:
	if(word in D.keys()):
		D[word] = D[word] + 1
	else
	
SyntaxError: invalid syntax
>>> for word in L:
	if(word in D.keys()):
		D[word] = D[word] + 1
	else:
		D[word] = 1

		
>>> D
{'red': 3, 'yellow': 2, 'green': 1}
>>> Z = Counter(L)
>>> Z
Counter({'red': 3, 'yellow': 2, 'green': 1})
>>> Z["yellow"]
2
>>> 
>>> # ----------------------------------- operator
>>> 
>>> from operator import itemgetter
>>> 
>>> itemgetter(1)("apples")
'p'
>>> itemgetter(1)(["red", "green", "blue"])
'green'
>>> f = itemgetter(1)
>>> type(f)
<class 'operator.itemgetter'>
>>> 
>>> f("apples")
'p'
>>> f(["red", "green", "blue"])
'green'
>>> 
>>> L = ["red", "green", "blue"]
>>> L.sort(key=f)
>>> L
['red', 'blue', 'green']
>>> L.sort(key=itemgetter(-1))
>>> L
['red', 'blue', 'green']
>>> 
