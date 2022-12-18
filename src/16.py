import sys
S={(v:=l.split())[1]:[int(v[4][5:-1]),{w[:2]for w in v[9:]}] for l in open(sys.argv[1])}
R=lambda S,n,v,t:{e:t+1 for e in n if S[e][0]*t}|R(S,{e for f in n for e in S[f][1]-v},v|n,t+1)if n else{}
r={p:[R(S,{p},set(),0),1<<i]for i,p in enumerate(S)}
def T(M,t,Q=r["AA"][0],o=0,s=0):M[s]=max(M.get(s,0),o);[T(M,u,r[q][0],u*S[q][0]+o,s+b)for q in Q if not (b:=r[q][1])&s and(u:=t-Q[q])>0]
E={};T(E,26);M={};T(M,30)
print([max(M.values()),max(E[e]+E[h]for e in E for h in E if not h&e)])
