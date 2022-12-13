import sys
import functools
from numpy import integer
infile = sys.argv[1] 
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
pairs = []
part2_pairs = []
p1 = p2 = None
inorder_pairs = 0
index = 0
for line in lines:
    if index % 3 == 0:
        p1 = eval(line)
    if index % 3 == 1:
        p2 = eval(line)
        pairs.append((p1, p2))
        part2_pairs.append(p1)
        part2_pairs.append(p2)

    index += 1

def recurse_compare(o1, o2):
    if type(o1) == int and type(o2) == int:
        
        if o1 < o2:
            return -1
        elif o1 == o2:
            return 0
        else:
            return 1
    elif type(o1) == list and type(o2) == list:
        index1 = 0
        index2 = 0
        while index1 < len(o1) or index2 < len(o2):
            if index1 == len(o1) and index2 < len(o2):
                return -1
            elif index1 < len(o1) and index2 == len(o2):
                return 1
            else:
                current_e1 = o1[index1]
                current_e2 = o2[index2]
                print(index1, index2)
                if type(current_e1) == int and type(current_e2) == list: 
                    current_e1 = [current_e1]
                elif type(current_e1) == list and type(current_e2) == int: 
                    current_e2 = [current_e2]
                
                if recurse_compare(current_e1, current_e2) == 1:
                    return 1
                elif recurse_compare(current_e1, current_e2) == -1:
                    return -1
                
            index1 += 1
            index2 += 1
        
        return 0
  
for i, p in enumerate(pairs):

    if recurse_compare(p[0], p[1]) == -1:
        inorder_pairs += (i + 1)

i1 = i2 = 0
for i, pair in enumerate(sorted(part2_pairs, key=functools.cmp_to_key(recurse_compare))):
    if pair == [[2]]:
        i1 = i + 1
    elif pair == [[6]]:
        i2 = i + 1







            


