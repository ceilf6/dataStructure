ma = {}

n = int(input())

vis = set() # 已经声明的变量

mid = [',','=']

for _ in range(n):
    # 先判断是否有效
    
    temp = input().split()

    flag=1

    tempvis = set()
    tempma = {}
    #for i in range(len(temp)):
    i=0
    while i < len(temp):
        if temp[i] == 'int':
            #tog = 0
            #for j in range(i+1,len(temp)):
            j = 0
            while j<len(temp[i+1]):
                if temp[i+1][j] == ';':
                    break
                if temp[i+1][j] not in mid: #and tog%2==0:
                    if temp[i+1][j] in vis or temp[i+1][j] in tempvis:
                        flag=0
                        break
                    else:
                        #print(temp,j)
                        
                        tempvis.add(temp[i+1][j])
                        if temp[i+1][j+1]=='=':
                            if temp[i+1][j+2] not in tempvis:
                                if temp[i+1][j+2] not in vis:
                                    if ord(temp[i+1][j+2])>ord('0') and ord(temp[i+1][j+2])<ord('9'):
                                        tempma[temp[i+1][j]]=temp[i+1][j+2]
                                    else:
                                        flag=0
                                        break
                                else:
                                    #print(ma,temp[i+1][j+2])
                                    #print(tempma)
                                    tempma[temp[i+1][j]]=ma[temp[i+1][j+2]]
                            else:
                                if tempma[temp[i+1][j+2]]!='undefined':
                                    print(1)
                                    tempma[temp[i+1][j]]=tempma[temp[i+1][j+2]]
                                else:
                                    flag=0
                                    break
                            j=j+3
                        else:
                            tempma[temp[i+1][j]]='undefined'
                j+=1
            i=i+2
        else:
            a=temp[i+1][0]
            b=temp[i+1][2]
            if a not in tempvis and a not in vis:
                flag=0
                break
            if b not in tempvis:
                if b not in vis:
                    if ord(b)>ord('0') and ord(b)<ord('9'):
                        tempma[a]=b
                    else:
                        flag=0
                        break
                else:
                    tempma[a]=ma[b]
            else:
                tempma[a]=tempma[b]
            i=i+4
                
        if flag==0:
            break

    if flag==0:
        continue
    for i in tempma:
        ma[i]=tempma[i]
    for i in tempvis:
        vis.add(i)

for i in ma:
    print(i,ma[i])
