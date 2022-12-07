import sys
c=C=(0,)
F={}
for l in open(sys.argv[1]):
	p,_,*n=l.split()
	if n:c={"/":C,".":c[:-1]}.get(l[5],c+(*n,))
	if p.isdigit():
		d=c
		while d:F[d]=F.get(d,0)+int(p);d=d[:-1]
S=F.values()
print([sum(x for x in S if x<1e5),min(x for x in S if x>F[C]-4e7)])
