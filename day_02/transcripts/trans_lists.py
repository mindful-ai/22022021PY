Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["Red", "green", 12, 12.56, int(), ['a', 'b', 'c']]
>>> type(L)
<class 'list'>
>>> L[0]
'Red'
>>> L[-1]
['a', 'b', 'c']
>>> L[-2]
0
>>> L[-2]("1010", 2)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    L[-2]("1010", 2)
TypeError: 'int' object is not callable
>>> L[-2]
0
>>> type(L[-2])
<class 'int'>
>>> L[-2] = int
>>> L
['Red', 'green', 12, 12.56, <class 'int'>, ['a', 'b', 'c']]
>>> L[-2] = int()
>>> L
['Red', 'green', 12, 12.56, 0, ['a', 'b', 'c']]
>>> L[-2] = int
>>> L
['Red', 'green', 12, 12.56, <class 'int'>, ['a', 'b', 'c']]
>>> L = [int, str, list, tuple, set, max, min]
>>> L
[<class 'int'>, <class 'str'>, <class 'list'>, <class 'tuple'>, <class 'set'>, <built-in function max>, <built-in function min>]
>>> 
>>> 
>>> 
>>> # ------------------------------ subscripting
>>> 
>>> L = ['red', 'green' , 'blue', 'yellow']
>>> L
['red', 'green', 'blue', 'yellow']
>>> L[0]
'red'
>>> L[2]
'blue'
>>> L[-1]
'yellow'
>>> L[1:3]
['green', 'blue']
>>> L[-3:-1]
['green', 'blue']
>>> L[:2]
['red', 'green']
>>> L[:]
['red', 'green', 'blue', 'yellow']
>>> L[::-1]
['yellow', 'blue', 'green', 'red']
>>> L[::2]
['red', 'blue']
>>> 
>>> # -------------------------- operators
>>> 
>>> L[1::2]
['green', 'yellow']
>>> 
>>> L[::3]
['red', 'yellow']
>>> 
>>> 
>>> L1 = ["black", "grey", "white"]
>>> L + L1
['red', 'green', 'blue', 'yellow', 'black', 'grey', 'white']
>>> L
['red', 'green', 'blue', 'yellow']
>>> L1
['black', 'grey', 'white']
>>> 
>>> L * 3
['red', 'green', 'blue', 'yellow', 'red', 'green', 'blue', 'yellow', 'red', 'green', 'blue', 'yellow']
>>> len(L + L1)
7
>>> "red" in L + L1
True
>>> True
True
>>> "red" in L1
False
>>> 
>>> L is list
False
>>> isinstance(L, list)
True
>>> type(L) is list
True
>>> del L1
>>> L1
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    L1
NameError: name 'L1' is not defined
>>> 
>>> # -----------------------------
>>> 
>>> N = 90
>>> N is int
False
>>> type(N) is int
True
>>> ytpe(N)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    ytpe(N)
NameError: name 'ytpe' is not defined
>>> type(N)
<class 'int'>
>>> 
>>> # ------------------------------ Mutability
>>> 
>>> L
['red', 'green', 'blue', 'yellow']
>>> 
>>> L[2]
'blue'
>>> L[2] = "orange"
>>> L
['red', 'green', 'orange', 'yellow']
>>> L[2]
'orange'
>>> L[2][2]
'a'
>>> L[2][2] = "y"
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    L[2][2] = "y"
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> L
['red', 'green', 'orange', 'yellow']
>>> L[2] = ["black", "white"]
>>> L
['red', 'green', ['black', 'white'], 'yellow']
>>> 
>>> 
>>> L
['red', 'green', ['black', 'white'], 'yellow']
>>> L = ['red', 'green', 'orange', 'yellow']
>>> L
['red', 'green', 'orange', 'yellow']
>>> L[2]
'orange'
>>> L[2:3]
['orange']
>>> L[2:3] = ["black", "white"]
>>> L
['red', 'green', 'black', 'white', 'yellow']
>>> L[4:5]
['yellow']
>>> L[4:5] = [ ["lightblue", "blue"], "red"]
>>> L
['red', 'green', 'black', 'white', ['lightblue', 'blue'], 'red']
>>> 
>>> 
>>> # ------------------------- add elements
>>> 
>>> L
['red', 'green', 'black', 'white', ['lightblue', 'blue'], 'red']
>>> L = ['red', 'green', "blue"]
>>> L
['red', 'green', 'blue']
>>> L.append("yellow")
>>> L
['red', 'green', 'blue', 'yellow']
>>> L.append("golden")
>>> L
['red', 'green', 'blue', 'yellow', 'golden']
>>> L.insert(-2, "orange")
>>> L
['red', 'green', 'blue', 'orange', 'yellow', 'golden']
>>> L.insert(3, "brown")
>>> L
['red', 'green', 'blue', 'brown', 'orange', 'yellow', 'golden']
>>> L.insert5(20, "hue")
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    L.insert5(20, "hue")
AttributeError: 'list' object has no attribute 'insert5'
>>> L.insert(20, "hue")
>>> L
['red', 'green', 'blue', 'brown', 'orange', 'yellow', 'golden', 'hue']
>>> 
>>> L1 = ["black", "white", "grey"]
>>> L1
['black', 'white', 'grey']
>>> L.extend(L1)
>>> L
['red', 'green', 'blue', 'brown', 'orange', 'yellow', 'golden', 'hue', 'black', 'white', 'grey']
>>> 

>>> # -------------------------------- removing elements
>>> 
>>> L.pop()
'grey'
>>> L.pop()
'white'
>>> L.pop(4)
'orange'
>>> "brown" in L
True
>>> L.remove("BROWN".lower())
>>> L
['red', 'green', 'blue', 'yellow', 'golden', 'hue', 'black']
>>> 
>>> 
>>> L[3:6]
['yellow', 'golden', 'hue']
>>> L[3:6] = []
>>> L
['red', 'green', 'blue', 'black']
>>> # ------------------------- Sanjeeth -> Removing a section of the list
>>> 
>>> # ------------------------------------- Re-arranging elements
>>> 
>>> L
['red', 'green', 'blue', 'black']
>>> 
>>> L.reverse()
>>> L
['black', 'blue', 'green', 'red']
>>> reversed(L)
<list_reverseiterator object at 0x0000023711B2FE48>
>>> list(reversed(L))
['red', 'green', 'blue', 'black']
>>> L
['black', 'blue', 'green', 'red']
>>> 
>>> 
>>> L
['black', 'blue', 'green', 'red']
>>> L.sort()
>>> L
['black', 'blue', 'green', 'red']
>>> L.sort(reverse=True)
>>> L
['red', 'green', 'blue', 'black']
>>> sorted(L)
['black', 'blue', 'green', 'red']
>>> L
['red', 'green', 'blue', 'black']
>>> 
>>> 
>>> L
['red', 'green', 'blue', 'black']
>>> import random
>>> random.shuffle(L)
>>> L
['black', 'red', 'blue', 'green']
>>> 
>>> 
>>> 
>>> #--------------------------- Arun
>>> 
>>> L = [('Blue', 'Pink'), 'black', 'orange', 'green', 'red']
>>> L.sort()
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    L.sort()
TypeError: '<' not supported between instances of 'str' and 'tuple'
>>> L.sort(key=lambda x : x[0])
>>> L
[('Blue', 'Pink'), 'black', 'green', 'orange', 'red']
>>> # ------------- Krishnamurthy
>>> 
>>> 
>>> 
>>> random.choice(L)
'black'
>>> random.choice(L)
'red'
>>> 
>>> 
>>> 
>>> # ---------------------------------------- searching
>>> 
>>> L
[('Blue', 'Pink'), 'black', 'green', 'orange', 'red']
>>> 'green' in L
True
>>> L.index("green")
2
>>> L[2]
'green'
>>> L.count("green")
1
>>> L.count("GreeN",lower())
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    L.count("GreeN",lower())
NameError: name 'lower' is not defined
>>> L.count("GreeN".lower())
1
>>> L.append("green")
>>> L.count("green")
2
>>> # ------------------------------ iteration
>>> 
>>> L
[('Blue', 'Pink'), 'black', 'green', 'orange', 'red', 'green']
>>> for item in L:
	print(item)

	
('Blue', 'Pink')
black
green
orange
red
green
>>> for item in L:
	if(type(item) is str):
		print(item.upper())

		
BLACK
GREEN
ORANGE
RED
GREEN
>>> YelloW.lower()
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    YelloW.lower()
NameError: name 'YelloW' is not defined
>>> 'YelloW'.lower() in L
False
>>> # --------------------- Prakash
>>> 
>>> # --------------------------------------- Copying lists
>>> 
>>> L = ['red', 'green', 'blue', 'black']
>>> 
>>> L
['red', 'green', 'blue', 'black']
>>> L1 = L
>>> L
['red', 'green', 'blue', 'black']
>>> L1
['red', 'green', 'blue', 'black']
>>> 
>>> L1.append("yellow")
>>> L1
['red', 'green', 'blue', 'black', 'yellow']
>>> 
>>> L
['red', 'green', 'blue', 'black', 'yellow']
>>> 
>>> 
>>> L2 = L[:]
>>> L2.append("black")
>>> L2
['red', 'green', 'blue', 'black', 'yellow', 'black']
>>> L
['red', 'green', 'blue', 'black', 'yellow']
>>> 
>>> import copy
>>> L3 = copy.deepcopy(L)
>>> L
['red', 'green', 'blue', 'black', 'yellow']
>>> L3
['red', 'green', 'blue', 'black', 'yellow']
>>> L.append("white")
>>> L
['red', 'green', 'blue', 'black', 'yellow', 'white']
>>> L3
['red', 'green', 'blue', 'black', 'yellow']
>>> 
