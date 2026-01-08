k=[13,1,2,3,5,4,4,2,2,2]

y1=[31,28,31,30,31,30,31,31,30,31,30,31]
y2=[31,29,31,30,31,30,31,31,30,31,30,31]

summm=0
for i in range(2000,2024):
    if i%4==0:
        for j in range(1,13):
            for z in range(1,y2[j-1]+1):
                if j>=10 and z>=10:
                    s=str(i)+str(j)+str(z)
                elif j<10 and z<10:
                    s=str(i)+'0'+str(j)+'0'+str(z)
                elif j<10 and z>=10:
                    s=str(i)+'0'+str(j)+str(z)
                elif j>=10 and z<10:
                    s=str(i)+str(j)+'0'+str(z)
                #print(s)
                summ=0    
                for f in s:
                    #print(f)
                    summ+=k[int(f)]
                if summ>50:
                    summm+=1
    else:
        for j in range(1,13):
            for z in range(1,y1[j-1]+1):
                if j>=10 and z>=10:
                    s=str(i)+str(j)+str(z)
                elif j<10 and z<10:
                    s=str(i)+'0'+str(j)+'0'+str(z)
                elif j<10:
                    s=str(i)+'0'+str(j)+str(z)
                else:
                    s=str(i)+str(j)+'0'+str(z)

                summ=0    
                for f in s:
                    summ+=k[int(f)]
                if summ>50:
                    summm+=1


i=2024
for j in range(1,5):
    if j<4:
        for z in range(1,y2[j-1]+1):
            if j>=10 and z>=10:
                s=str(i)+str(j)+str(z)
            elif j<10 and z<10:
                s=str(i)+'0'+str(j)+'0'+str(z)
            elif j<10:
                s=str(i)+'0'+str(j)+str(z)
            else:
                s=str(i)+str(j)+'0'+str(z)

            summ=0    
            for f in s:
                summ+=k[int(f)]
            if summ>50:
                summm+=1
    if j==4:
        for z in range(1,14):
            if j>=10 and z>=10:
                s=str(i)+str(j)+str(z)
            elif j<10 and z<10:
                s=str(i)+'0'+str(j)+'0'+str(z)
            elif j<10:
                s=str(i)+'0'+str(j)+str(z)
            else:
                s=str(i)+str(j)+'0'+str(z)

            summ=0    
            for f in s:
                summ+=k[int(f)]
            if summ>50:
                summm+=1

print(summm)
