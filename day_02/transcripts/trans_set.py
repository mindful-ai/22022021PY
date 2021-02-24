Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "mississippi"
>>> L = list(s)
>>> T = tuple(s)
>>> S = set(s)
>>> L
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> T
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> S
{'i', 's', 'm', 'p'}
>>> type(S)
<class 'set'>
>>> 
>>> 
>>> s1 = set("abcdefgh")
>>> s1
{'d', 'h', 'f', 'a', 'g', 'b', 'c', 'e'}
>>> s2 = {'f', 'g', 'h', 'i', 'j', 'h', 'k'}
>>> s2
{'h', 'k', 'f', 'i', 'j', 'g'}
>>> 
>>> 
>>> s1[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s1[0]
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> # ------------------------------- operators
>>> 
>>> s1 | s2
{'d', 'h', 'k', 'f', 'a', 'j', 'i', 'g', 'b', 'c', 'e'}
>>> s1 & s2
{'h', 'g', 'f'}
>>> s1 ^ s2
{'d', 'k', 'a', 'i', 'j', 'b', 'c', 'e'}
>>> 
>>> # ------------------------------ functions
>>> 
>>> s1
{'d', 'h', 'f', 'a', 'g', 'b', 'c', 'e'}
>>> s1.add("x")
>>> s1
{'d', 'h', 'f', 'a', 'x', 'g', 'b', 'c', 'e'}
>>> s3 = {'y', 'z', 'x'}
>>> s1.update(s3)
>>> s1
{'d', 'h', 'f', 'a', 'y', 'x', 'z', 'g', 'b', 'c', 'e'}
>>> s1.remove('h')
>>> s1
{'d', 'f', 'a', 'y', 'x', 'z', 'g', 'b', 'c', 'e'}
>>> 
