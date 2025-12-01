
import csv

with open('input', 'r') as f:
    csvr = csv.reader(f, delimiter=' ')
    lines = list(csvr)
    lines = [l[0] for l in lines]

pos=50
base=100
target=0
counter=0
passing_counter=0
for l in lines:
    d = int(l[1:])
    if d==0 and pos==0:
        continue
    if l[0]=='R':
        pos += d
        passing_counter+=pos//base
        print(pos,pos//base, passing_counter)
    else:
        pos -= d
        _pos = 100-pos
        passing_counter+=_pos//base
        if pos+d==0:
            print(pos,d)
            passing_counter-=1 # ew
        print(pos,_pos//base, passing_counter)
    
    pos = pos%base
    if pos==target:
        counter+=1
#




    
print(counter)
print(passing_counter)
