
import os
import sys

import re
import bisect
'''
pattern='hello'
string='hello wjh'

result=re.match(pattern, string, flags=1)

result = re.search(r'\d+', 'abc123def456')

result=result.group()
print(result)
'''




k = int(input())
s = input()

'''
lista = [m.start() for m in re.finditer(r"\bAlice\b",s)]
'''
f = "Alice"
lista = [m.start() for m in re.finditer(rf"\b{re.escape(f)}\b", s)]



listb = [m.start() for m in re.finditer(r"\bBob\b",s)]
print(lista,listb)
count = 0
for i in range(len(lista)):
    lo = bisect.bisect_right(listb, lista[i]-k-3)
    up = bisect.bisect_right(listb, lista[i]+k+5)
    count += up-lo
print(count)
