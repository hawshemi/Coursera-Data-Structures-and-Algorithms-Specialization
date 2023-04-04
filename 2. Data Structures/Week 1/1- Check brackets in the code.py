
def fun(l):
    if len(l)==0:
        return 'Success'
    symbolarray=('(',')','{','}','[',']')
    start=('(','[','{')
    dictionary={'(':')','{':'}','[':']'}
    stack=[]
    index=[]
    for i in range(len(l)):
        if l[i] in symbolarray:
            if l[i] in start:
                stack.append(l[i])
                index.append(i)
            else:
                if not stack or l[i]!=dictionary[stack[-1]]:
                    return i+1
                else:
                    stack.pop()
                    index.pop()
    if len(stack)==0:
        return 'Success'
    else:
        return index[0]+1
    
    
    
l=list(input())
print(fun(l))