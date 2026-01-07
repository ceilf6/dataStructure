n=int(input())

s=[[i+1 for i in range(n)]for j in range(n)]
for i in range(1,n):
    for j in range(n):
        if j==0:
            s[i][j]=i
            continue
        if j==i:
            s[i][j]=i*n+2-i
        elif j>i:
            s[i][j]=s[i][j-1]+1
        else:
            s[i][j]=s[j][i-1]
'''
for j in range(n):
    s[-1][j]=(j+1)*n-j-1
'''
output='\n'.join(' '.join(map(str,x)) for x in s)

print(output)
