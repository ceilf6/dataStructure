s=input()

minn=float('inf')
for i in range(len(s)-2):
    minn=min(minn,abs(int(s[i:i+3])-753))

print(minn)
