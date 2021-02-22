Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "python"
>>> type(s)
<class 'str'>
>>> 
>>> # -------------------------- Operators
>>> 
>>> s + "perl"
'pythonperl'
>>> s * 3
'pythonpythonpython'
>>> len(s)
6
>>> "th" in s
True
>>> "app" in s
False
>>> 
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> s = "python"
>>> s is int
False
>>> s is str
False
>>> isinstance(s, str)
True
>>> a = 10
>>> isinstance(a, int)
True
>>> type(s) is str
True
>>> type(a) is int
True
>>> type(a) is float
False
>>> type(a)
<class 'int'>
>>> 
>>> 
>>> # ----------------------------- Sub scripting
>>> 
>>> # Immutable Aspect of the strings
>>> 
>>> s
'python'
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[0] = 'x'
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s[0] = 'x'
TypeError: 'str' object does not support item assignment
>>> a = 'xython'
>>> 
>>> 
>>> # Subscripts
>>> 
>>> s = a
>>> s
'xython'
>>> s = "python"
>>> s
'python'
>>> 
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[2]
't'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[-3]
'h'
>>> len(s)
6
>>> 
>>> s[1:3]
'yt'
>>> s[1:4]
'yth'
>>> s[-5:-2]
'yth'
>>> s[-2:-5]
''
>>> 
>>> 
>>> s
'python'
>>> s[10]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s[10]
IndexError: string index out of range
>>> len(s)
6
>>> s[6]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s[6]
IndexError: string index out of range
>>> s[5]
'n'
>>> s[4:6]
'on'
>>> s[4:7]
'on'
>>> s[4:8]
'on'
>>> s[7]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s[7]
IndexError: string index out of range
>>> s[8]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s[8]
IndexError: string index out of range
>>> 
>>> 
>>> 
>>> s
'python'
>>> s[0:4]
'pyth'
>>> s[:4]
'pyth'
>>> s[3:6]
'hon'
>>> s[3:]
'hon'
>>> s[:]
'python'
>>> s[0:6]
'python'
>>> s[0:6:2]
'pto'
>>> s[::2]
'pto'
>>> s[::3]
'ph'
>>> s[::-1]
'nohtyp'
>>> s[1:-3]
'yt'
>>> 
>>> 
>>> 
>>> s = "computer"
>>> s[::-1]
'retupmoc'
>>> s[::-2]
'rtpo'
>>> 
>>> 
>>> s[1:6]
'omput'
>>> s[1:6:2]
'opt'
>>> s[1:6:-1]
''
>>> s[1:6][::-1]
'tupmo'
>>> 
>>> 
>>> # ---------------------------- string functions
>>> 
>>> 
>>> s
'computer'
>>> s[2::2]
'mue'
>>> # ----------- Sanjeeth
>>> 
>>> # -------------------------- case
>>> 
>>> s
'computer'
>>> s.upper()
'COMPUTER'
>>> s.lower()
'computer'
>>> s.capitalize()
'Computer'
>>> 
>>> # --------------------------- serach
>>> 
>>> 'p' in s
True
>>> 
>>> s.find('p')
3
>>> s.count('e')
1
>>> 
>>> m = "mississippi"
>>> m.count("s")
4
>>> m.count("ss")
2
>>> # ---------------------------  validating
>>> 
>>> a = "123"
>>> a.isdigit()
True
>>> a.isalpha()
False
>>> a.isalnum()
True
>>> 
>>> f = "123.45"
>>> f.isdigit()
False
>>> g = "#$dff"
>>> g.isalnum()
False
>>> 
>>>  ' '.isspace()
 
SyntaxError: unexpected indent
>>> ' '.isspace()
True
>>> 
>>> # -------------------------- modifications
>>> 
>>> m
'mississippi'
>>> k = "     34 "
>>> k.strip()
'34'
>>> s.lstrip()
'computer'
>>> k.lstrip()
'34 '
>>> k.rstrip()
'     34'
>>> 
>>> 
>>> s
'computer'
>>> s.ljust(30)
'computer                      '
>>> s.rjust(30)
'                      computer'
>>> s.ljust(30,'>')
'computer>>>>>>>>>>>>>>>>>>>>>>'
>>> 
>>> 
>>> ip = "192-168-1-1"
>>> ip.replace('-','.')
'192.168.1.1'
>>> ip
'192-168-1-1'
>>> 
>>> #ip = ip.replace()
>>> newip = ip.replace('-','.')
>>> ip
'192-168-1-1'
>>> newip
'192.168.1.1'
>>> 
>>> 
>>> text = "mary had a little lamb"
>>> text.split()
['mary', 'had', 'a', 'little', 'lamb']
>>> L = ['mary', 'had', 'a', 'little', 'lamb']
>>> type(L)
<class 'list'>
>>> '-'.join(L)
'mary-had-a-little-lamb'
>>> 'XYZ'.join(L)
'maryXYZhadXYZaXYZlittleXYZlamb'
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> len(text.split('a'))
5
>>> # --------------------------------------- serach
>>> 
>>> site = "www.google.com"
>>> site.endswith("org")
False
>>> site.startswith("www")
True
>>> "google" in site
True
>>> site.split('.')[1]
'google'
>>> # ---------------- Achal
>>> 
>>> s[4:10]
'uter'
>>> site[4:10]
'google'
>>> site[4:10][::-1]
'elgoog'
>>> site.split('.')[1]
'google'
>>> site.split('.')[1][::-1]
'elgoog'
>>> 
>>> 
>>> # ------------ iteration
>>> 
>>> for c in s:
	print(c)

	
c
o
m
p
u
t
e
r
>>> for c in s:
	print(c, end=' ')

	
c o m p u t e r 
>>> for c in s:
	print(c, end='')

	
computer
>>> 
