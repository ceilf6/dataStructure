n,q=map(int,input().split())

a=[0]+list(map(int,input().split()))

x=[0]*q
p=[0]*q
cao=[[]for i in range(q)]
for i in range(q):
    '''
    x[i],p[i]=map(int,input().split())
    '''
    cao[i]=list(map(int,input().split()))

def yl(x,p):
    
    for j in range(1,n+1):
        if (x-abs(j-p))>0:
            a[j]=max(0,a[j]-(x-abs(j-p)))
            
def f_p(arr):
    peaks = []
    if a[1]>a[2]:
        peaks.append(a[1])
    for i in range(2, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks.append(arr[i])
    if a[-1]>a[-2]:
        peaks.append(a[-1])
    return peaks

def f_v(arr):
    valleys = []
    if a[1]<a[2]:
        valleys.append(a[1])
    for i in range(2, len(arr) - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            valleys.append(arr[i])
    if a[-1]<a[-2]:
        valleys.append(a[-1])
    return valleys
'''
def ans():
    for 
'''


#ans()
print(-sum(f_v(a))+sum(f_p(a)))
for i in range(q):
    yl(cao[i][0],cao[i][1])
    print(a)
    print(f_v(a),f_p(a))
    print(-sum(f_v(a))+sum(f_p(a)))

