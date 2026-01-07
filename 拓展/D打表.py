
n=1000

pre=[1]

ans=[1]

for i in range(2,n):
    ans.append(i**2-pre[-1])
    pre.append(i**2)

print(ans)
