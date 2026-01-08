
a=0
b=1
summ=0
for  i in range(1,1000000):
    a+=i
    b*=i
    if (a-b)%100==0:
        summ+=1

print(summ)
#print(2024041331404202//100)
