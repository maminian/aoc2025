
import csv
import numpy as np
import math


with open('input_mini', 'r') as f:
    #csvr = csv.reader(f, delimiter=' ')
    #lines = list(csvr)
    #lines = [l[0] for l in lines]
    lines = f.readlines()
    lines = [l.strip('\n') for l in lines]
    lines_h = [l.split() for l in lines]



def add(ll):
    return sum([int(l) if l.strip()!='' else 0 for l in ll])
def mult(ll):
    return math.prod([int(l) if l.strip()!='' else 1 for l in ll])

ops = {'*':mult, '+':add}
#

s = 0
for tup in zip(*lines_h):
    s += ops[tup[-1]](tup[:-1])
print(s)

# cephalapod math

# refactor
# scan lengths of fields
ps = []
c=0
for l in lines[-1]:
    if l!=' ':
        ps.append(c)
    c+=1
ps.append(len(lines[0]))

# re-identify problems and input
c = 0
for i in range(len(ps)-1):
    # extract problem block
    l,r = ps[i:i+2]
    block = [line[l:r] for line in lines[:-1]]
    o = lines[-1][l]
    flat = ''.join(block)
    
    step = r-l
    numbers = []

#    for b in block:
#        print(b)
    # misread; i'm both reading the block backward and reversing. whoops
    for start in range(len(flat)-step,len(flat)):
        num = ''.join([flat[k] for k in range(start,-1,-step)])
        num = num[::-1]
        numbers.append(num)
#    print('')

    # re-apply operation
    c += ops[o](numbers)

print(c) # part 2

