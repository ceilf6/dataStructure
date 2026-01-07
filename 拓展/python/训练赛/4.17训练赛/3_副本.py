s=input()
if len(s)>=6:
    print(s[:4]+'-'+s[4:])
else:
    if s[:2]<'22':
        print('20'+s[:2]+'-'+s[2:])
    else:
        print('19'+s[:2]+'-'+s[2:])
