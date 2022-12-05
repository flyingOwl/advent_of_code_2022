import sys
s,i=[x.split('\n')[:-1] for x in open(sys.argv[1]).read().split("\n\n")]
D=[[*filter(str.strip,[*zip(*s)][j])] for j in range(-3,len(s[0]),4)]
E=[z[:] for z in D]
def F(D,j):
	for a,s,t in [map(int,l.split()[1::2]) for l in i]:
		D[t][:0]=D[s][:a][::j];del D[s][:a]
	return "".join(next(zip(*D[1:])))
print([F(D,-1),F(E,1)])
