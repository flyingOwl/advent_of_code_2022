import sys
F=set()
I=lambda r,i:r+i*1j;E=lambda x:(x>0)-(x<0);D=lambda x:I(E(x.real),E(x.imag))
for l in open(sys.argv[1]):
	L=[I(*map(int,j.split(','))) for j in l.split('->')];G=L.pop()
	while L:
		g=L.pop();d=D(g-G);F|={G}
		while G!=g:G+=d;F|={G}
M=max(g.imag for g in F)+1
def f(V,s):[f(V,p) for p in [s+1j,s-1+1j,s+1+1j] if not(p in F or p in V or p.imag>M)];V[s]=len(V)
V={};f(V,500);print([min(V[k] for k in V if k.imag==M),len(V)])
