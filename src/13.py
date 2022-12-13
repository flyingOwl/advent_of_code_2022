import sys
t=type
def C(a,b):
	if t(a)==t(b)==int:return a-b
	if t(a)==int:a=[a]
	if t(b)==int:b=[b]
	return x if (x:=next(filter(bool,map(C,a,b)),0)) else len(a)-len(b)
L=[eval(l) for l in open(sys.argv[1]) if l.strip()]
s=sum(1+i//2 for i in range(0,len(L),2) if C(*L[i:i+2])<0)
x=lambda e,s:sum(C(a,[[e]])<0 for a in L)+s
print([s,x(2,1)*x(6,2)])
