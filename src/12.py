import sys
M={};L={};e=enumerate
for y,l in e(open(sys.argv[1])):
	for x,c in e(l[:-1]):p=x+y*1j;L[c]=p;M[p]=[ord(c)-97,26*(c<'S')][c<'a']
def F(P):
	s=0;V=P
	while L['E'] not in P:V|=P;s+=1;P={p+d for p in P for d in [-1,1,-1j,1j] if p+d not in V and M.get(p+d,99)<M[p]+2}
	return s
print([F({L['S']}),F({p for p in M if M[p]==0})])
