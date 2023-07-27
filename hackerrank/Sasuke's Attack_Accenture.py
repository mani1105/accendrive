n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(len(l)):
    if((l[i]-k)>0):
        l[i]=l[i]-k
    else:
        l[i]=0
print(max(l))
    
