a,b,n=map(int,input().split())

m=1
'''
while(1):
  if 6>m%7>0 and n-a>0:
    n-=a
    m+=1
  elif n-b>0:
    n-=b
    m+=1
  else:
    break
'''
#一天天运算太慢了，整合为一周进行运算

print(m)
