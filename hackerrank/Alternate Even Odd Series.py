n=input()       
t=0
e=[]
o=[]
for i in n:
    if(i.isdigit()):
        if(int(i)%2)==0:
            e.append(i)
        else:
            o.append(i)
    else:
        if not (i.isalpha()):
            t=t+1
l=max(len(e),len(o))
res=[]
if(t%2)==0:
    for j in range(l):
        if(j<len(e)):
            res.append(e[j])
        if(j<len(o)):
            res.append(o[j])
else:
    for j in range(l):
        if(j<len(o)):
            res.append(o[j])
        if(j<len(e)):
            res.append(e[j])
print(''.join(str(i) for i in res))
