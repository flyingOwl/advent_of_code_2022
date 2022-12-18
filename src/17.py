import sys
R=range
Z=[[0,3,1,2],[1+2j,2+1j,1,1j],[2+2j,2,0,1,2+1j],[3j,0,1j,2j],[1+1j,0,1j,1]]
S=[ord(c)-61 for c in open(sys.argv[1]).read()[:-1]]
g=lambda i,X:((i+1)%len(X),X[i])
B={*R(7)};t=v=i=A=m=0;C={}
while i<1e12:
	i+=1;s=2+(m+4)*1j;t,r=g(t,Z)
	if i==2023:z=m;A=1
	if A==1:
		c=(*(i+j*1j in B for j in R(m-9,m) for i in R(7)),t,v)
		if c in C:l,n=C[c];j=int(1e12-i)//(I:=i-l);A=j*(m-n);i+=j*I
		C[c]=(i,m)
	while 1:
		v,w=g(v,S);s+=w*all(0<=(P:=s+p+w).real<7 and P not in B for p in r)
		if {s+p-1j for p in r}&B:B|={s+p for p in r};break
		s-=1j
	m=max(m,int((s+r[0]).imag))
print([z,m+A])
