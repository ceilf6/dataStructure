while True:
    try:
        n=2024
        k=0
        if n==2024:
            i=n
            summ=0
            if i%2==0:#偶
                summ+=(1+i//2-1)*(i//2-1)//2
                summ+=i//4
            else:
                summ+=(1+i//2)*(i//2)//2
            summ+=i
            k=max(k,summ)
        print(k)
    except EOFError:
        break
