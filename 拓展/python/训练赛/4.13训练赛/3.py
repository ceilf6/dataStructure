n=int(input())

if n<=100:
    if n%10!=0:
        n=(n//10*10)
    else:
        n=(n-10)
else:
    n=(100)

print("Gong xi nin! Nin de ti zhong yue wei: {n} duo jin")
