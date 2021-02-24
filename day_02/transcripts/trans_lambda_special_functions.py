Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = lambda x,y : x + y
>>> type(f)
<class 'function'>
>>> f(10, 20)
30
>>> f("py","th")
'pyth'
>>> f([1,2,3], [4,5,6])
[1, 2, 3, 4, 5, 6]
>>> 
>>> # ---------------------------- map()
>>> 
>>> T = [100, 34, 56, 99]
>>> F = []
>>> for temp in T:
	F.append(temp * 1.8 + 32)

	
>>> F
[212.0, 93.2, 132.8, 210.20000000000002]
>>> 
>>> F1 = map(lambda t : t * 1.8 + 32, T)
>>> F1
<map object at 0x000001F1C5679D30>
>>> list(F1)
[212.0, 93.2, 132.8, 210.20000000000002]
>>> 
>>> 
>>> # --------------------------------- filter
>>> 
>>> import random
>>> RN = []
>>> for i in range(100):
	RN.append(random.randint(1, 100))

	
>>> RN
[50, 66, 91, 98, 65, 16, 47, 1, 91, 66, 32, 67, 12, 59, 17, 27, 13, 72, 65, 36, 25, 38, 32, 38, 11, 46, 26, 13, 7, 100, 19, 61, 21, 86, 68, 32, 17, 89, 43, 12, 34, 82, 19, 36, 27, 3, 91, 55, 24, 11, 76, 40, 10, 33, 95, 83, 46, 20, 7, 13, 68, 30, 68, 24, 43, 21, 85, 58, 83, 44, 51, 48, 83, 99, 100, 7, 34, 77, 48, 85, 34, 44, 7, 69, 46, 20, 100, 13, 60, 98, 76, 71, 41, 77, 7, 52, 60, 92, 82, 97]
>>> 
>>> N7 = []
>>> for n in RN:
	if(n % 7 == 0):
		N7.append(n)

		
>>> N7
[91, 98, 91, 7, 21, 91, 7, 21, 7, 77, 7, 98, 77, 7]
>>> N71 = filter(lambda n : (n % 7 == 0), RN)
>>> N71
<filter object at 0x000001F1C5675780>
>>> list(N71)
[91, 98, 91, 7, 21, 91, 7, 21, 7, 77, 7, 98, 77, 7]
>>> 
>>> 
>>> # ---------------------------------- sort
>>> 
>>> L = ["zebra", "cat", "antelope", "yak", "monkey"]
>>> L.sort()
>>> L
['antelope', 'cat', 'monkey', 'yak', 'zebra']
>>> L.sort(key=lambda s : s[-1])
>>> L
['zebra', 'antelope', 'yak', 'cat', 'monkey']
>>> 
>>> T = [ (1, "apples"), (2, "banana"), (5, "grapes"), (3, "figs"), (2, "berry")]
>>> T.sort()
>>> T
[(1, 'apples'), (2, 'banana'), (2, 'berry'), (3, 'figs'), (5, 'grapes')]
>>> T = [ (1, "apples"), (2, "banana"), (5, "grapes"), (3, "figs"), (4, "berry")]
>>> T.sort()
>>> T
[(1, 'apples'), (2, 'banana'), (3, 'figs'), (4, 'berry'), (5, 'grapes')]
>>> T.sort(key=lambda item : item[1])
>>> T
[(1, 'apples'), (2, 'banana'), (4, 'berry'), (3, 'figs'), (5, 'grapes')]
>>> 
>>> 
>>> # -------------------------------------------- zip
>>> 
>>> T1 = ( "anil", "sunil", "raj")
>>> T2 = ( "bangalore", "pune", "delhi")
>>> zip(T1, T2)
<zip object at 0x000001F1C571B888>
>>> dict(zip(T1, T2))
{'anil': 'bangalore', 'sunil': 'pune', 'raj': 'delhi'}
>>> list(zip(T1, T2))
[('anil', 'bangalore'), ('sunil', 'pune'), ('raj', 'delhi')]
>>> 
>>> 
>>> D = {'anil': 'bangalore', 'sunil': 'pune', 'raj': 'delhi'}
>>> D.items()
dict_items([('anil', 'bangalore'), ('sunil', 'pune'), ('raj', 'delhi')])
>>> zip(*D.items())
<zip object at 0x000001F1C571B5C8>
>>> list(zip(*D.items()))
[('anil', 'sunil', 'raj'), ('bangalore', 'pune', 'delhi')]
>>> 
