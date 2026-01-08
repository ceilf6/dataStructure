a=1
b=1
n=0
for i in range(120):
    #print((a+b)%10)
    b=(a+b)%10
    a=(b-a)%10
    if b==7:
        n+=1
print(n)
