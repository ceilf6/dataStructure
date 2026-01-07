
def main():
    #code here
    t=int(input())
    for _ in range(t):
        n=int(input())
        wait=[]
        for i in range(n):
            temp=list(map(int,input().split()))
            if temp[0]==1:
                wait.append([temp[1]+1,n])
            elif temp[0]==2:
                wait.append([1,temp[1]+1])
            else:
                wait.append([temp[1]+1,temp[2]+1])

        wait=sorted(wait,key=lambda x:(x[0],x[1]))
        #print(wait)
        flag=1
        for i in range(n):
            if i+1<wait[i][0] or i+1>wait[i][1]:
                flag=0
                print('N')
                break
        if flag:
            print('Y')
    pass


if __name__ == '__main__':
    main();
