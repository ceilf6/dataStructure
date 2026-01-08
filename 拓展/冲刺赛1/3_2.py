
for i in range(2010,4040):
    summ=0
    if i<=2023:
        if i%2==0:#偶
            summ+=(1+i//2-1)*(i//2-1)//2
            summ+=i//4
        else:
            summ+=(1+i//2)*(i//2)//2
            summ+=i
    elif i>2023:
        if i%2==0:#偶
            summ+=(i-2023+i//2-1)*(i//2-(i-2023))//2
            summ+=i//4
        else:
            summ+=(i-2023+i//2)*(i//2-(i-2023)+1)//2
    print(summ)
