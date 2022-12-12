import sys
M={};L={};e=enumerate
for y,l in e(open(sys.argv[1])):
	for x,c in e(l[:-1]):p=x+y*1j;L[c]=p;M[p]=[ord(c)-97,26*(c<'S')][c<'a']
s=0;V={};P={L['E']}
while L['S'] not in P:
	V|={p:s for p in P};s+=1;P={p+d for p in P for d in [-1,1,-1j,1j] if p+d not in V and M.get(p+d,-2)+2>M[p]}
print([s,min(V[p] for p in V if M[p]==0)])
