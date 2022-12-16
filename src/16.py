import sys
S={(v:=l.split())[1]:[int(v[4][5:-1]),{w.strip(',') for w in v[9:]}] for l in open(sys.argv[1])}
def R(S,p):
	s=1
	v={p}
	d={}
	n=S[p][1]
	while n:
		s+=1;v|=n;m=set()
		for e in n:
			if S[e][0]:d[e]=s
			m|=S[e][1]
		n=m-v
	return d
r={p:R(S,p) for p in S}
P="AA"
def T(M,p,t,o):
	Q=r[p]
	M[tuple(o.keys())]=sum(S[k][0]*v for k,v in o.items())
	for q in Q.keys()-o.keys():
		if t>Q[q]:T(M,q,t-Q[q],{q:t-Q[q]}|o)
M={}
T(M,P,30,{})
N={};E={}
T(N,P,26,{})
for n in sorted(N,key=N.get):
	E[tuple(sorted(n))]=N[n]
MM=max(x+y for e,x in E.items() for h,y in E.items() if not set(h)&set(e))
print([max(M.values()),MM])
