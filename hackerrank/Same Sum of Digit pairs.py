from collections import Counter
lst=list(map(int,input().split(",")))
st=set(lst)
def par(x):
    return(x*(x-1))//2
def sum(n):
    t=0
    while(n>0):
        t=t+n%10
        n=n//10
    return t
l=[]
s=[]
for i in st:
    l.append(sum(i))
d=Counter(l)
ans=0
for i in d:
    if d[i]>1:
        ans=ans+par(d[i])
print(ans)
    
