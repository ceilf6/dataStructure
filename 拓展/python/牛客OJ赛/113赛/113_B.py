n=int(input())
s=input()

i=0
summ=0
while i<len(s)-1:
    if s[i]==s[i+1]:
        summ+=1
        i+=1
    if summ>=2:
        print('NO')
        break
    i+=1

if summ<=1:
    print('YES')
