
import csv
import numpy as np

with open('input', 'r') as f:
    csvr = csv.reader(f, delimiter=' ')
    lines = list(csvr)
    lines = [l[0] for l in lines]

_d={'.':0,'@':1}
m = len(lines)
n = len(lines[0])
A = np.zeros((m+2,n+2))
A[1:-1,1:-1] = np.array([[_d[z] for z in line] for line in lines], dtype=int)

########
# part 1
surr = np.zeros((m+2,n+2))
for i in range(1,m+1):
    for j in range(1,n+1):
        surr[i,j] = np.sum(A[i-1:i+2,j-1:j+2]) - A[i,j]

accessible = np.where(A*(surr<4)>0)
print( len(accessible[0]) )

# part 2

import itertools

count=0
to_remove = list(zip(*accessible))
while len(to_remove)>0:
    i,j = to_remove.pop(0)
    A[i,j]=0
    count+=1
    l,r=max(i-1,0),min(i+2,m+2)
    d,u=max(j-1,0),min(j+2,n+2)
    nbrs = list(itertools.product(range(l,r), range(d,u)))
    nbrs.remove((i,j))
    for p,q in nbrs:
        surr[p,q] -= 1
        if surr[p,q] < 4 and A[p,q]==1 and (not (p,q) in to_remove):
            to_remove.append((p,q))

print(count)
