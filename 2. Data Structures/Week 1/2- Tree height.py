
def fun(n,l):
    cache=[0]*n
    for i in range(n):
        if l[i]==-1:
            cache[i]=1
        else:
            tmp=l[i]
            count=1
            while cache[tmp]==0:
                if l[tmp]==-1:
                    cache[tmp]=1
                    break
                tmp=l[tmp]
                count+=1
            cache[i]=cache[tmp]+count
    return max(cache)


n=int(input())
l=list(map(int, input().split()))
print(fun(n,l))