import sys
I=int;E=enumerate;M=max
L=[([I((v:=l.split())[30]),0,I(v[27])],[0,I(v[21]),I(v[18])],[0,0,I(v[12])],[0,0,I(v[6])]) for l in open(sys.argv[1])]
def S(B,t,z,A,X=0,N=[0]*7+[1]):
	m=N[0]+N[4]*t;a=(*N,t)
	if X>m+sum(range(t)) or a in A:return X
	m=M(X,m);A|={a}
	for i,b in E(B):
		if (i>0 and (z[i-1]<=N[4+i] or z[i-1]*t<N[i]))or(i<3 and N[i+1]==0):continue
		f=[((n-c-1)//g)+2 for c,g,n in zip(N,N[4:],[0]+b) if c<n];F=M(f+[1])
		if all(f) and F<=t:n=[F*g+c-n for c,g,n in zip(N,N[4:],[0]+b)]+N[4:];n[i+4]+=1;m=M(m,S(B,t-F,z,A,m,n))
	return m
a,b,c=[S(B,32,[*map(M,zip(*B))],set())for B in L[:3]]
print([sum(i*S(B,24,[*map(M,zip(*B))],set())for i,B in E(L,1)),a*b*c])
