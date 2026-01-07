def manacher(s):
    t='#'+'#'.join(s)+'#'
    '''
    在开头、中间、结尾加入 # 消除奇偶长度的区分
    '''

    n=len(t)
    p=[0]*n     #回文半径
    R=C=max_len=center=0
    #R:当前“蘑菇”覆盖翼展最右端位置
    #C:翼展最右的中心位置
    #max_len、center表征最大的蘑菇

    for i in range(n):
        p[i]=min(p[2*C-i],R-i) if R-i>0 else 0
        #取小者：镜像位置，当前最右覆盖

        while i+p[i]+1<n and i-p[i]-1>=0\
              and t[i+p[i]+1]==t[i-p[i]-1]:
            #暴力向两边拓展判断：如果相等那么就半径加一
            p[i]+=1

        if p[i]+i>R:
            C,R=i,i+p[i]

        if p[i]>max_len:#记录最大蘑菇
            max_len,center=p[i],i
            
    return s[(center-max_len)//2:(center+max_len)//2]

print(manacher('aba'))
