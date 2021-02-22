Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> type(a)
<class 'int'>
>>> a = 5.5
>>> type(a)
<class 'float'>
>>> 
>>> # -----------------------------
>>> 
>>> n1 = -1.234
>>> n2 = 3/4
>>> n3
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    n3
NameError: name 'n3' is not defined
>>> n2
0.75
>>> n3 = Fraction(3, 4)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    n3 = Fraction(3, 4)
NameError: name 'Fraction' is not defined
>>> 
>>> # ---------------------------------------- NUMBERS
>>> 
>>> 
>>> a = 5
>>> b = 2
>>> 
>>> # ----------------- Operators
>>> 
>>> # Arithmetic operators
>>> 
>>> a + b
7
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> a % b
1
>>> a // b
2
>>> a ** b
25
>>> c = a ** b
>>> print(c)
25
>>> d = c - a
>>> print(d)
20
>>> # Relational Operators
>>> 
>>> a > b # Is a greater than b?
True
>>> a < b
False
>>> a >= b
True
>>> a <= b
False
>>> a == b * 2 + 1
True
>>> a != 8
True
>>> a != 5
False
>>> 
>>> # Logical operators
>>> 
>>> (a >= 5) and (a != 10)
True
>>> a
5
>>> (a >= 5) and (b < 2)
False
>>> (a >= 5) or (b < 2)
True
>>> (a >= 5) or not (b < 2)
True
>>> # ----------------------- Built in functions
>>> 
>>> b - a
-3
>>> a - b
3
>>> abs(b - a)
3
>>> abs(a - b)
3
>>> s = "12"
>>> 
>>> type(s)
<class 'str'>
>>> s + a
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s + a
TypeError: can only concatenate str (not "int") to str
>>> int(s) + a
17
>>> s = "100"
>>> int(s)
100
>>> hex(s)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    hex(s)
TypeError: 'str' object cannot be interpreted as an integer
>>> hex(100)
'0x64'
>>> bin(100)
'0b1100100'
>>> oct(100)
'0o144'
>>> pow(10, 3)
1000
>>> floor(5/3)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    floor(5/3)
NameError: name 'floor' is not defined
>>> c = 1.23456
>>> round(c, 2)
1.23
>>> 
>>> 
>>> d = "11101"
>>> int(d)
11101
>>> b = "1111"
>>> int(b) + 10
1121
>>> int(b, base=2)
15
>>> int(b, 2)
15
>>> int(b, 2) + 10
25
>>> len(a)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    len(a)
TypeError: object of type 'int' has no len()
>>> len(d)
5
>>> # -------------------------------- Built in modules
>>> 
>>> ang = 90
>>> sin(ang)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    sin(ang)
NameError: name 'sin' is not defined
>>> import math
>>> sin(ang)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    sin(ang)
NameError: name 'sin' is not defined
>>> math.sin(ang)
0.8939966636005579
>>> math.sin(ang *( 3.14/180))
0.9999996829318346
>>> math.sin(ang *( 3.14159/180))
0.9999999999991198
>>> math.sin(ang * math.pi/180)
1.0
>>> math.sin(math.radians(ang))
1.0
>>> # ---------------------------------------------- INPUTS
>>> 
>>> input()
12
'12'
>>> i = input()
12
>>> i
'12'
>>> int(i) + 19
31
>>> i + 19
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    i + 19
TypeError: can only concatenate str (not "int") to str
>>> type(i)
<class 'str'>
>>> i = input("Enter a number: ")
Enter a number: 12
>>> int(i) + 5
17
>>> i = int(input("Enter a number: "))
Enter a number: 12
>>> i
12
>>> i + 10
22
>>> 
