Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = ("red", "blue", "green", ["black", "white"])
>>> type(T)
<class 'tuple'>
>>> 
>>> # ------------------------ Operators
>>> 
>>> T + ("cyan", "brown")
('red', 'blue', 'green', ['black', 'white'], 'cyan', 'brown')
>>> T
('red', 'blue', 'green', ['black', 'white'])
>>> 
>>> T * 3
('red', 'blue', 'green', ['black', 'white'], 'red', 'blue', 'green', ['black', 'white'], 'red', 'blue', 'green', ['black', 'white'])
>>> "red" in T
True
>>> type(T) is tuple
True
>>> isinstance(T, tuple)
True
>>> # del T
>>> 
>>> # ------------------------------- subscripting
>>> 
>>> T[0]
'red'
>>> T[0] = "blue"
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    T[0] = "blue"
TypeError: 'tuple' object does not support item assignment
>>> T[2:4]
('green', ['black', 'white'])
>>> T[::2]
('red', 'green')
>>> T[::-1]
(['black', 'white'], 'green', 'blue', 'red')
>>> T
('red', 'blue', 'green', ['black', 'white'])
>>> 
>>> 
>>> # --------------------------------- re-arrangement
>>> 
>>> T
('red', 'blue', 'green', ['black', 'white'])
>>> T.reverse()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    T.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> reversed(T)
<reversed object at 0x000001B0C0FC5780>
>>> list(reversed(T))
[['black', 'white'], 'green', 'blue', 'red']
>>> sorted(T)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    sorted(T)
TypeError: '<' not supported between instances of 'list' and 'str'
>>> T1 = ('red', 'blue', 'green', "Agate")
>>> sorted(T1)
['Agate', 'blue', 'green', 'red']
>>> 
>>> # ------------------------- how to change/modify a list
>>> 
>>> T
('red', 'blue', 'green', ['black', 'white'])
>>> T = list(T)
>>> T
['red', 'blue', 'green', ['black', 'white']]
>>> T.append("golden")
>>> T
['red', 'blue', 'green', ['black', 'white'], 'golden']
>>> T = tuple(T)
>>> T
('red', 'blue', 'green', ['black', 'white'], 'golden')
>>> 
>>> 
>>> # ------------------------------- one observation
>>> 
>>> T
('red', 'blue', 'green', ['black', 'white'], 'golden')
>>> T[3]
['black', 'white']
>>> T[3].append("grey")
>>> T
('red', 'blue', 'green', ['black', 'white', 'grey'], 'golden')
>>> 
>>> 
>>> L = ["red", "green", "blue", ("black", "white")]
>>> L[1] = "lisghtgreen"
>>> L
['red', 'lisghtgreen', 'blue', ('black', 'white')]
>>> L[-1]
('black', 'white')
>>> L[-1].append("grey")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    L[-1].append("grey")
AttributeError: 'tuple' object has no attribute 'append'
>>> 
>>> L[-1]
('black', 'white')
>>> A = list(L[-1])
>>> A.append("grey")
>>> A
['black', 'white', 'grey']
>>> L[-1] = tuple(A)
>>> L
['red', 'lisghtgreen', 'blue', ('black', 'white', 'grey')]
>>> 
>>> 
>>> # ---------------------
>>> 
>>> a = 10
>>> a = str(a)
>>> 
