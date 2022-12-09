import sys
M=[0,-1,-1,1,1];R=[-2,-1,0,1,2]
A={(a:=i+j*1j):[0,M[i]+M[j]*1j][abs(a)>=2] for i in R for j in R}
P=set();Q=set();H=0;T=[0]*9
for l in open(sys.argv[1]):
	d={'R':1,'L':-1,'U':1j,'D':-1j}[l[0]];i=int(l[2:])
	while i:
		H+=d;i-=1;u=H;j=0
		for k in T:T[j]=u=k+A[k-u];j+=1
		P|={T[0]};Q|={u}
print([len(P),len(Q)])
