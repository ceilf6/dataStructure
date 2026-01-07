t=int(input())

for i in range(t):
    n=int(input())
    s=input()

    n1=s.count('1')
    n0=s.count('0')

    print(n1*(n-1)+n0)
