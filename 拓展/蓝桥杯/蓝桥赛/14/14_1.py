y1=[31,28,31,30,31,30,31,31,30,31,30,31]
y2=[31,29,31,30,31,30,31,31,30,31,30,31]

summ=0

for i in range(1900,10000):
    if (i%4==0 and i%100!=0) or i%400==0:
        for j in range(1,13):
            for z in range(1,y2[j-1]+1):
                k1=i
                k2=j
                k3=z
                sum1=0
                sum2=0
                while k1:
                    sum1+=k1%10
                    k1//=10
                while k2:
                    sum2+=k2%10
                    k2//=10
                while k3:
                    sum2+=k3%10
                    k3//=10
                if sum1==sum2:
                    summ+=1
    else:
        for j in range(1,13):
            for z in range(1,y1[j-1]+1):
                k1=i
                k2=j
                k3=z
                sum1=0
                sum2=0
                while k1:
                    sum1+=k1%10
                    k1//=10
                while k2:
                    sum2+=k2%10
                    k2//=10
                while k3:
                    sum2+=k3%10
                    k3//=10
                if sum1==sum2:
                    summ+=1

print(summ)
