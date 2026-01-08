Len=[]

def lenn(a1,a2):
    A1=a1+a1
    A2=a2+a2

    i=0
    j=0

    Lenn=[]
    for i in range(len(a1)):
        for j in range(len(a2)):
            if A1[i]==A2[j]:
                l1=i
                l2=j
                summ=1
                
                while l1+summ<len(A1) and l2+summ<len(A2):
                    if A1[l1+summ]==A2[l2+summ]:
                        summ+=1
                    else:
                        '''
                        r1=i+summ-1#在没不匹配，自然退出时：r1和r2没有赋值！！！
                        r2=j+summ-1
                        '''
                        break
                r1=i+summ-1
                r2=j+summ-1
                
                    
                '''
                while l1+summ<len(A1) and l2+summ<len(A2) and A1[l1+summ]==A2[l2+summ]:
                        summ+=1
                r1=i+summ-1
                r2=j+summ-1
                #print(l1,r1,summ)
                '''

                if r1>len(a1)-1:
                    len1=len(a1)-l1
                else:
                    len1=r1-l1+1
                if r2>len(a2)-1:
                    len2=len(a2)-l2
                else:
                    len2=r2-l2+1

                Lenn.append(max(len1,len2))
                print(Lenn)
    Len.append(max(Lenn))

    #print(Lenn)
    #Len.append(min(max(Lenn),m))

#lenn('abba','aabb')


lenn('aaaaa','snkad')
print(Len)

