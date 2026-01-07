P=list(map(float,input().split()))

py=P[3]+P[4]

pN=pow(1-py,10)+10*pow(1-py,9)*py

pY=1-pN

print(pY)
