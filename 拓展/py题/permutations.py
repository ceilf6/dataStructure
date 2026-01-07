from itertools import permutations
'''
l=['a','b','c']

l2=[]
for i in range(1,len(l)+1):
    l2=[''.join(p) for p in permutations(l,i)]

print(l2)
'''

l=[1,2,3]

for i in range(1,len(l)+1):
    l2=[''.join(map(str,p)) for p in permutations(l,i)]

print(l2)
