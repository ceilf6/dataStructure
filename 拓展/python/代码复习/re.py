s='dssashAlice Alice ???Alice'

f='Alice'
import re
lis=[m.start() for m in re.finditer(rf"\b{re.escape(f)}\b",s)]

print(lis)
