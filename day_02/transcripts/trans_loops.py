Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LOOPS
>>> 
>>> for c in "aeiou":
	print(c)

	
a
e
i
o
u
>>> for item in ["red", "green", "blue"]:
	print(item)

	
red
green
blue
>>> for item in ("red", "green", "blue"):
	print(item)

	
red
green
blue
>>> for item in {"red", "green", "blue", "red", "red"}:
	print(item)

	
blue
red
green
>>> D = {"name":"Anil", "age":35, "country":"India"}
>>> for item in D:
	print(item)

	
name
age
country
>>> for k in D.keys():
	print(k)

	
name
age
country
>>> for v in D.values():
	print(v)

	
Anil
35
India
>>> for kv in D.items():
	print(kv)

	
('name', 'Anil')
('age', 35)
('country', 'India')
>>> 
>>> # ----------------------- unpacking
>>> 
>>> a, b, c = ("red", "green", "blue")
>>> a
'red'
>>> b
'green'
>>> c
'blue'
>>> a, b = ("red", "green", "blue")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a, b = ("red", "green", "blue")
ValueError: too many values to unpack (expected 2)
>>> a, b, *x = ("red", "green", "blue", "yellow", "cyan")
>>> a
'red'
>>> b
'green'
>>> x
['blue', 'yellow', 'cyan']
>>> 
>>> 
>>> for k, v D.items():
	
SyntaxError: invalid syntax
>>> for k, v in D.items():
	print(k, ' ---> ', v)

	
name  --->  Anil
age  --->  35
country  --->  India
>>> for k, v in D.items():
	print(v, ' ---> ', k)

	
Anil  --->  name
35  --->  age
India  --->  country
>>> D1 = {}
>>> for k, v in D.items():
	D1.setdefault(v, k)

	
'name'
'age'
'country'
>>> D1
{'Anil': 'name', 35: 'age', 'India': 'country'}
>>> 
>>> # ------------------------------------------ multiplication table
>>> 
>>> N = 5
>>> print(N, " X ", 1, " = ", N*1)
5  X  1  =  5
>>> I = [1, 2, 3, 4, 5]
>>> for i in I:
	print(N, " X ", i, " = ", N*i)

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(10, 30, 2))
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
>>> list(range(20, 10, -1))
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
>>> list(range(20, 10, -2))
[20, 18, 16, 14, 12]
>>> 
>>> for i in range(1, 11):
	print(N, " X ", i, " = ", N*i)

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> # ----------------------------------- loop controls
>>> 
>>> for i in range(10):
	if(i % 3 == 0):
		break
	print(i, end=' ')

	
>>> for i in range(1,10):
	if(i % 3 == 0):
		break
	print(i, end=' ')

	
1 2 
>>> for i in range(1,10):
	if(i % 3 == 0):
		continue
	print(i, end=' ')

	
1 2 4 5 7 8 
>>> 
>>> # ----------------------------------- While loop
>>> 
>>> for x, y, z in ("red", "green", "blue"):
	print(x)
	print(y)
	print(z)

	
r
e
d
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    for x, y, z in ("red", "green", "blue"):
ValueError: too many values to unpack (expected 3)
>>> for x, y, *z in ("red", "green", "blue"):
	print(x)
	print(y)
	print(z)

	
r
e
['d']
g
r
['e', 'e', 'n']
b
l
['u', 'e']
>>> 
>>> 
>>> x = "red"
>>> x
'red'
>>> x, y, z = "red"
>>> x
'r'
>>> y
'e'
>>> z
'd'
>>> for x, y, z in (("red", "green", "blue")):
	print(x)
	print(y)
	print(z)

	
r
e
d
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    for x, y, z in (("red", "green", "blue")):
ValueError: too many values to unpack (expected 3)
>>> for x, y, z in [("red", "green", "blue")]:
	print(x)
	print(y)
	print(z)

	
red
green
blue
>>> for x, y, z in (("red", "green", "blue")):
	print(x)
	print(y)
	print(z)

	
r
e
d
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    for x, y, z in (("red", "green", "blue")):
ValueError: too many values to unpack (expected 3)
>>> for x in (("red", "green", "blue")):
	print(x)

	
red
green
blue
>>> for x in (('red', 'green', 'blue')):
	print(x)

	
red
green
blue
>>> for x in (('red', 'green', 'blue'), ('red', 'green', 'blue'), ('red', 'green', 'blue')):
	print(x)

	
('red', 'green', 'blue')
('red', 'green', 'blue')
('red', 'green', 'blue')
>>> for x, y, z in (('red', 'green', 'blue'), ('red', 'green', 'blue'), ('red', 'green', 'blue')):
	print(x, y, z)

	
red green blue
red green blue
red green blue
>>> 
>>> 
>>> # ------------------------ While loop
>>> 
>>> i = 1
>>> while i <= 10:
	print(N, " X ", i, " = ", N*i)
	i += 1

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> i
11
>>> i++
SyntaxError: invalid syntax
>>> i += 1
>>> i
12
>>> 
