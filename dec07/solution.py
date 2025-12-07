
import csv
import numpy as np


with open('input_mini', 'r') as f:
    csvr = csv.reader(f, delimiter=' ')
    lines = list(csvr)
    lines = [list(l[0]) for l in lines]

A = np.array(lines)
i0=0
j0 = np.where(A[0]=='S')[0][0]

active = set([j0])
splits = 0
for i in range(1,len(A)):
    line = A[i]
    new = []
    splitters=np.where(line=='^')[0]
    for s in splitters:
        if s in active:
            splits += 1
            active.remove(s)
            active.add(s-1)
            active.add(s+1)

print(splits)

# part 2
cache = {}
splitters = np.where(A=='^')
bycol={}
for _i,_j in zip(*splitters):
    bycol[_j] = bycol.get(_j, []) + [_i]

def perc(_i,_j, imax=A.shape[1]):
    # fetch next fork point
    if _j not in bycol:
        return 1
    forks = bycol[_j]
    fork=False
    for f in forks:
        if f>_i:
            fork=True
            break
    if fork:
        cache[(f,_j-1)]=cache.get((f,_j-1), perc(f,_j-1))
        cache[(f,_j+1)]=cache.get((f,_j+1), perc(f,_j+1))
        return cache[(f,_j-1)]+cache[(f,_j+1)]
    else:
        cache[(_i,_j)]=1
        return 1

if True:
    # unusably slow
    part2 = perc(i0,j0)



print(part2)
