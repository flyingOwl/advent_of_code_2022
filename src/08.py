import sys
e=enumerate
def F(X,Y,x,y):
	L=[X[:x],X[:x:-1],Y[:y],Y[:y:-1]];h=0;s=1;v=X[x]
	for l in L:
		t=0;u=1
		while u and l:u&=l.pop()<v;t+=1
		h|=u;s*=t
	return h,s
T=[[*map(int,l[:-1])] for l in open(sys.argv[1])];U=zip(*T)
A,B=zip(*[F(t,[*u],x,y) for x,u in e(U) for y,t in e(T)])
print([sum(A),max(B)])
