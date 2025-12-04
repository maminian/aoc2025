
import csv

with open('input_mini', 'r') as f:
    csvr = csv.reader(f, delimiter=' ')
    lines = list(csvr)
    lines = [l[0] for l in lines]

########
# part 1

def pointy(line,t,o):
    print(line)
    for i in range(len(line)):
        print('^' if i in [t,o] else ' ', end='')
    print()

joltages=[]
for line in lines:
    n = len(line)
    ti=n-2
    oi=n-1
    tens=line[ti]
    ones=line[oi]
    l=n-2
    for i in range(ti,-1,-1):
        if line[i]>=tens:
            tens=line[i]
            ti=i
    for i in range(oi,ti,-1):
        if line[i]>=ones:
            ones=line[i]
            oi=i
#    pointy(line,ti,oi)
    joltages.append(int(line[ti]+line[oi]))

print(sum(joltages))


########
# part 2

def pointy(line,t,o):
    print(line)
    for i in range(len(line)):
        print('^' if i in [t,o] else ' ', end='')
    print()

joltages2=[]
for line in lines:
    n = len(line)
    pointers=list(range(n-12,n))
    digits=[line[p] for p in pointers]
    l=-1
    for k in range(12):
        p = pointers[k]
        r = pointers[k]
        for i in range(r,l,-1):
            if line[i]>=line[p]:
                p=i
                digits[k]=line[p]
        l=p
    numba = int(''.join(digits))
    joltages2.append(numba)

print(sum(joltages2))

############
# visualization
from matplotlib import pyplot as plt
from matplotlib import patches,collections
import numpy as np
import itertools

plt.style.use('dark_background')

colors = plt.cm.vanimo(np.linspace(0,1,12))

#

arr = np.array([[int(l) for l in line] for line in lines], dtype=int)

fig,ax = plt.subplots(figsize=(5,10))

# static elements
[s.set_visible(False) for s in ax.spines.values()]
ax.set(xticks=[], yticks=[])

for i,j in itertools.product(range(arr.shape[0]), range(arr.shape[1])):
    ax.text(j,i,lines[i][j], fontsize=4, zorder=100, ha='center', va='center')

ax.set(xlim=[0,100],ylim=[0,200])

##
squares=[]
for j, line in enumerate(lines):
    n = len(line)
    pointers=list(range(n-12,n))
#    squares=[patches.Rectangle((j,p),1,1,edgecolor=[0,0,0,0], facecolor=colors[k]) for k,p in enumerate(pointers)]
    squares += [patches.Rectangle((j,p),1,1,edgecolor=None, facecolor=colors[k]) for k,p in enumerate(pointers)]
    #ax.add_collection(collections.PatchCollection(squares, match_original=True))
    
    digits=[line[p] for p in pointers]
    l=-1
    for k in range(12):
        p = pointers[k]
        r = pointers[k]
        for i in range(r,l,-1):
            if line[i]>=line[p]:
                p=i
                digits[k]=line[p]
        l=p
    numba = int(''.join(digits))
    joltages2.append(numba)

ax.add_collection(collections.PatchCollection(squares, match_original=True, zorder=-100))



fig.show()

