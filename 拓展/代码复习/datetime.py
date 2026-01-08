import datetime

s=input()

dt2=datetime.datetime(2012,12,1,8,32,21)

t2=dt2.timestamp()

dt=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")

t=dt.timestamp()

ndt=dt+datetime.timedelta(days=2)

nt=ndt.timestamp()

print(t,t2,nt)
