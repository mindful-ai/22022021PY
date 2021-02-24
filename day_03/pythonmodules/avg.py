import sys

v = sys.argv[1:]

s = 0
for n in v:
    s += float(n)

print("AVERAGE :", s/len(v))

'''

(base) C:\Users\Purushotham\Desktop\oracle\day_03\pythonmodules>python cmdline_args.py 10 20 30 40 50
['cmdline_args.py', '10', '20', '30', '40', '50']

(base) C:\Users\Purushotham\Desktop\oracle\day_03\pythonmodules>python avg.py 10 20 30 40 50
AVERAGE : 30.0

'''