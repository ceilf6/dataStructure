for i in range(2024,1,-1):
    if 2024%i==0:
        for j in range(2,i):
            if i%j==0:
                break
        else:print(i)
