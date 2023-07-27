n=input()
m=input()
c=m[-2]+m[-1]
c=(eval(c)%4)+4
k=(eval(n[-1])**c)
strnum=repr(k)
print(strnum[-1])
