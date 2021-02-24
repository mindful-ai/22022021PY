Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # FILES
>>> 
>>> # open(), close()
>>> # read(), readline(), readlines()
>>> # write(), writelines()
>>> # seek(), tell()
>>> 
>>> f = open("C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\text.txt", "r")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
>>> path = "C:\next\text\signs\read.txt"
>>> print(path)
C:
ext	ext\signsead.txt
>>> path = r"C:\next\text\signs\read.txt"
>>> print(path)
C:\next\text\signs\read.txt
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\text.txt", "r")
>>> type(f)
<class '_io.TextIOWrapper'>
>>> 
>>> 
>>> content = f.read()
>>> print(content)
On a dark desert highway
Cool wind in my hair
Warm smell of colitas
Rising up through the air

Up ahead in the distance
I saw a shimmering light
My head grew heavy, and my sight grew dim
I had to stop for the night

There she stood in the doorway
I heard the mission bell
And I was thinking to myself:
"This could be heaven or this could be hell"

Then she lit up a candle
And she showed me the way
There were voices down the corridor
I thought I heard them say

Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face

Plenty of room at the Hotel California
Any time of year (any time of year)
You can find it here

Her mind is Tiffany-twisted
She got the Mercedes benz
She got a lot of pretty, pretty boys she calls friends

How they dance in the courtyard
Sweet summer sweat
Some dance to remember
Some dance to forget

So I called up the Captain:
"Please bring me my wine"
He said: "We haven't had that spirit here since 1969"

And still those voices are calling from far away
Wake you up in the middle of the night
Just to hear them say

Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face

They're living it up at the Hotel California
What a nice surprise (what a nice surprise)
Bring your alibis

Mirrors on the ceiling
The pink champagne on ice
And she said: "We are all just prisoners here of our own device"

And in the master's chambers
They gathered for the feast
They stab it with their steely knives
But they just can't kill the beast

Last thing I remember
I was running for the door
I had to find the passage back
To the place I was before

"Relax," said the night man
"We are programmed to receive
You can check out any time you like
But you can never leave"
>>> type(content)
<class 'str'>
>>> 
>>> 
>>> f.readline()
''
>>> f.tell()
1823
>>> len(content)
1753
>>> f.seek(0)
0
>>> f.readline()
'On a dark desert highway\n'
>>> f.readline()
'Cool wind in my hair\n'
>>> f.readline()
'Warm smell of colitas\n'
>>> 
>>> f.seek(0)
0
>>> f.readlines()
['On a dark desert highway\n', 'Cool wind in my hair\n', 'Warm smell of colitas\n', 'Rising up through the air\n', '\n', 'Up ahead in the distance\n', 'I saw a shimmering light\n', 'My head grew heavy, and my sight grew dim\n', 'I had to stop for the night\n', '\n', 'There she stood in the doorway\n', 'I heard the mission bell\n', 'And I was thinking to myself:\n', '"This could be heaven or this could be hell"\n', '\n', 'Then she lit up a candle\n', 'And she showed me the way\n', 'There were voices down the corridor\n', 'I thought I heard them say\n', '\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face\n', '\n', 'Plenty of room at the Hotel California\n', 'Any time of year (any time of year)\n', 'You can find it here\n', '\n', 'Her mind is Tiffany-twisted\n', 'She got the Mercedes benz\n', 'She got a lot of pretty, pretty boys she calls friends\n', '\n', 'How they dance in the courtyard\n', 'Sweet summer sweat\n', 'Some dance to remember\n', 'Some dance to forget\n', '\n', 'So I called up the Captain:\n', '"Please bring me my wine"\n', 'He said: "We haven\'t had that spirit here since 1969"\n', '\n', 'And still those voices are calling from far away\n', 'Wake you up in the middle of the night\n', 'Just to hear them say\n', '\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face\n', '\n', "They're living it up at the Hotel California\n", 'What a nice surprise (what a nice surprise)\n', 'Bring your alibis\n', '\n', 'Mirrors on the ceiling\n', 'The pink champagne on ice\n', 'And she said: "We are all just prisoners here of our own device"\n', '\n', "And in the master's chambers\n", 'They gathered for the feast\n', 'They stab it with their steely knives\n', "But they just can't kill the beast\n", '\n', 'Last thing I remember\n', 'I was running for the door\n', 'I had to find the passage back\n', 'To the place I was before\n', '\n', '"Relax," said the night man\n', '"We are programmed to receive\n', 'You can check out any time you like\n', 'But you can never leave"']
>>> 
>>> 
>>> f.close()
>>> 
>>> 
>>> content
'On a dark desert highway\nCool wind in my hair\nWarm smell of colitas\nRising up through the air\n\nUp ahead in the distance\nI saw a shimmering light\nMy head grew heavy, and my sight grew dim\nI had to stop for the night\n\nThere she stood in the doorway\nI heard the mission bell\nAnd I was thinking to myself:\n"This could be heaven or this could be hell"\n\nThen she lit up a candle\nAnd she showed me the way\nThere were voices down the corridor\nI thought I heard them say\n\nWelcome to the Hotel California\nSuch a lovely place (such a lovely place)\nSuch a lovely face\n\nPlenty of room at the Hotel California\nAny time of year (any time of year)\nYou can find it here\n\nHer mind is Tiffany-twisted\nShe got the Mercedes benz\nShe got a lot of pretty, pretty boys she calls friends\n\nHow they dance in the courtyard\nSweet summer sweat\nSome dance to remember\nSome dance to forget\n\nSo I called up the Captain:\n"Please bring me my wine"\nHe said: "We haven\'t had that spirit here since 1969"\n\nAnd still those voices are calling from far away\nWake you up in the middle of the night\nJust to hear them say\n\nWelcome to the Hotel California\nSuch a lovely place (such a lovely place)\nSuch a lovely face\n\nThey\'re living it up at the Hotel California\nWhat a nice surprise (what a nice surprise)\nBring your alibis\n\nMirrors on the ceiling\nThe pink champagne on ice\nAnd she said: "We are all just prisoners here of our own device"\n\nAnd in the master\'s chambers\nThey gathered for the feast\nThey stab it with their steely knives\nBut they just can\'t kill the beast\n\nLast thing I remember\nI was running for the door\nI had to find the passage back\nTo the place I was before\n\n"Relax," said the night man\n"We are programmed to receive\nYou can check out any time you like\nBut you can never leave"'
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\text2.txt", "w")
>>> f.write("HOTEL CALIFORNIA\n")
17
>>> f.writelines(["Eagles\n\n", "-"*50])
>>> f.close()
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\text2.txt", "a")
>>> f.write(content)
1753
>>> f,write("\n\n-------------------------------------\n\n")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    f,write("\n\n-------------------------------------\n\n")
NameError: name 'write' is not defined
>>> f.write("\n\n-------------------------------------\n\n")
41
>>> f.close()
>>> 
>>> 
>>> words = content.split()
>>> words
['On', 'a', 'dark', 'desert', 'highway', 'Cool', 'wind', 'in', 'my', 'hair', 'Warm', 'smell', 'of', 'colitas', 'Rising', 'up', 'through', 'the', 'air', 'Up', 'ahead', 'in', 'the', 'distance', 'I', 'saw', 'a', 'shimmering', 'light', 'My', 'head', 'grew', 'heavy,', 'and', 'my', 'sight', 'grew', 'dim', 'I', 'had', 'to', 'stop', 'for', 'the', 'night', 'There', 'she', 'stood', 'in', 'the', 'doorway', 'I', 'heard', 'the', 'mission', 'bell', 'And', 'I', 'was', 'thinking', 'to', 'myself:', '"This', 'could', 'be', 'heaven', 'or', 'this', 'could', 'be', 'hell"', 'Then', 'she', 'lit', 'up', 'a', 'candle', 'And', 'she', 'showed', 'me', 'the', 'way', 'There', 'were', 'voices', 'down', 'the', 'corridor', 'I', 'thought', 'I', 'heard', 'them', 'say', 'Welcome', 'to', 'the', 'Hotel', 'California', 'Such', 'a', 'lovely', 'place', '(such', 'a', 'lovely', 'place)', 'Such', 'a', 'lovely', 'face', 'Plenty', 'of', 'room', 'at', 'the', 'Hotel', 'California', 'Any', 'time', 'of', 'year', '(any', 'time', 'of', 'year)', 'You', 'can', 'find', 'it', 'here', 'Her', 'mind', 'is', 'Tiffany-twisted', 'She', 'got', 'the', 'Mercedes', 'benz', 'She', 'got', 'a', 'lot', 'of', 'pretty,', 'pretty', 'boys', 'she', 'calls', 'friends', 'How', 'they', 'dance', 'in', 'the', 'courtyard', 'Sweet', 'summer', 'sweat', 'Some', 'dance', 'to', 'remember', 'Some', 'dance', 'to', 'forget', 'So', 'I', 'called', 'up', 'the', 'Captain:', '"Please', 'bring', 'me', 'my', 'wine"', 'He', 'said:', '"We', "haven't", 'had', 'that', 'spirit', 'here', 'since', '1969"', 'And', 'still', 'those', 'voices', 'are', 'calling', 'from', 'far', 'away', 'Wake', 'you', 'up', 'in', 'the', 'middle', 'of', 'the', 'night', 'Just', 'to', 'hear', 'them', 'say', 'Welcome', 'to', 'the', 'Hotel', 'California', 'Such', 'a', 'lovely', 'place', '(such', 'a', 'lovely', 'place)', 'Such', 'a', 'lovely', 'face', "They're", 'living', 'it', 'up', 'at', 'the', 'Hotel', 'California', 'What', 'a', 'nice', 'surprise', '(what', 'a', 'nice', 'surprise)', 'Bring', 'your', 'alibis', 'Mirrors', 'on', 'the', 'ceiling', 'The', 'pink', 'champagne', 'on', 'ice', 'And', 'she', 'said:', '"We', 'are', 'all', 'just', 'prisoners', 'here', 'of', 'our', 'own', 'device"', 'And', 'in', 'the', "master's", 'chambers', 'They', 'gathered', 'for', 'the', 'feast', 'They', 'stab', 'it', 'with', 'their', 'steely', 'knives', 'But', 'they', 'just', "can't", 'kill', 'the', 'beast', 'Last', 'thing', 'I', 'remember', 'I', 'was', 'running', 'for', 'the', 'door', 'I', 'had', 'to', 'find', 'the', 'passage', 'back', 'To', 'the', 'place', 'I', 'was', 'before', '"Relax,"', 'said', 'the', 'night', 'man', '"We', 'are', 'programmed', 'to', 'receive', 'You', 'can', 'check', 'out', 'any', 'time', 'you', 'like', 'But', 'you', 'can', 'never', 'leave"']
>>> 
>>> D = {}
>>> for word in words:
	if(word in D.keys()):
		D[word] = D[word] + 1
	else:
		D[word] = 1

		
>>> D
{'On': 1, 'a': 12, 'dark': 1, 'desert': 1, 'highway': 1, 'Cool': 1, 'wind': 1, 'in': 6, 'my': 3, 'hair': 1, 'Warm': 1, 'smell': 1, 'of': 7, 'colitas': 1, 'Rising': 1, 'up': 5, 'through': 1, 'the': 24, 'air': 1, 'Up': 1, 'ahead': 1, 'distance': 1, 'I': 11, 'saw': 1, 'shimmering': 1, 'light': 1, 'My': 1, 'head': 1, 'grew': 2, 'heavy,': 1, 'and': 1, 'sight': 1, 'dim': 1, 'had': 3, 'to': 9, 'stop': 1, 'for': 3, 'night': 3, 'There': 2, 'she': 5, 'stood': 1, 'doorway': 1, 'heard': 2, 'mission': 1, 'bell': 1, 'And': 5, 'was': 3, 'thinking': 1, 'myself:': 1, '"This': 1, 'could': 2, 'be': 2, 'heaven': 1, 'or': 1, 'this': 1, 'hell"': 1, 'Then': 1, 'lit': 1, 'candle': 1, 'showed': 1, 'me': 2, 'way': 1, 'were': 1, 'voices': 2, 'down': 1, 'corridor': 1, 'thought': 1, 'them': 2, 'say': 2, 'Welcome': 2, 'Hotel': 4, 'California': 4, 'Such': 4, 'lovely': 6, 'place': 3, '(such': 2, 'place)': 2, 'face': 2, 'Plenty': 1, 'room': 1, 'at': 2, 'Any': 1, 'time': 3, 'year': 1, '(any': 1, 'year)': 1, 'You': 2, 'can': 3, 'find': 2, 'it': 3, 'here': 3, 'Her': 1, 'mind': 1, 'is': 1, 'Tiffany-twisted': 1, 'She': 2, 'got': 2, 'Mercedes': 1, 'benz': 1, 'lot': 1, 'pretty,': 1, 'pretty': 1, 'boys': 1, 'calls': 1, 'friends': 1, 'How': 1, 'they': 2, 'dance': 3, 'courtyard': 1, 'Sweet': 1, 'summer': 1, 'sweat': 1, 'Some': 2, 'remember': 2, 'forget': 1, 'So': 1, 'called': 1, 'Captain:': 1, '"Please': 1, 'bring': 1, 'wine"': 1, 'He': 1, 'said:': 2, '"We': 3, "haven't": 1, 'that': 1, 'spirit': 1, 'since': 1, '1969"': 1, 'still': 1, 'those': 1, 'are': 3, 'calling': 1, 'from': 1, 'far': 1, 'away': 1, 'Wake': 1, 'you': 3, 'middle': 1, 'Just': 1, 'hear': 1, "They're": 1, 'living': 1, 'What': 1, 'nice': 2, 'surprise': 1, '(what': 1, 'surprise)': 1, 'Bring': 1, 'your': 1, 'alibis': 1, 'Mirrors': 1, 'on': 2, 'ceiling': 1, 'The': 1, 'pink': 1, 'champagne': 1, 'ice': 1, 'all': 1, 'just': 2, 'prisoners': 1, 'our': 1, 'own': 1, 'device"': 1, "master's": 1, 'chambers': 1, 'They': 2, 'gathered': 1, 'feast': 1, 'stab': 1, 'with': 1, 'their': 1, 'steely': 1, 'knives': 1, 'But': 2, "can't": 1, 'kill': 1, 'beast': 1, 'Last': 1, 'thing': 1, 'running': 1, 'door': 1, 'passage': 1, 'back': 1, 'To': 1, 'before': 1, '"Relax,"': 1, 'said': 1, 'man': 1, 'programmed': 1, 'receive': 1, 'check': 1, 'out': 1, 'any': 1, 'like': 1, 'never': 1, 'leave"': 1}
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\text2.txt", "a")
>>> f.write("\n\n")
2
>>> for key in D.keys():
	w = key.ljust(20) + "|" + str(D[key]) + "\n"
	f.write(w)

	
23
24
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
24
23
23
23
23
24
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
23
>>> f.close()
>>> 
>>> s = "python"
>>> s.ljust(20)
'python              '
>>> 
