import sys
O=lambda x:"X L  J  G K IAHS  E   F       Y   RZOUB C P"[x%44]
L=[1];e=enumerate
for l in open(sys.argv[1]):
	L+=[L[-1]]
	if l[0]=="a":L+=[L[-1]+int(l[5:])]
S=sum(v*(20+i*40) for i,v in e(L[19::40]));A=[0]*8
for i,v in e(sum(v-2<j<v+2 for v in L[j:-1:40]) for j in range(40)):A[i//5]+=v<<2*(i%5)
print([S,"".join(map(O,A))])
