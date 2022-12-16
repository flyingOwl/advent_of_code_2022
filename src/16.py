import sys
S={(v:=l.split())[1]:[int(v[4][5:-1]),{w[:2]for w in v[9:]}] for l in open(sys.argv[1])}
R=lambda S,n,v,t:{e:t+1 for e in n if S[e][0]*t}|R(S,{e for f in n for e in S[f][1]-v},v|n,t+1)if n else{}
r={p:R(S,{p},set(),0)for p in S}
def T(M,t,Q=r["AA"],o={}):M[(*o,)]=sum(o.values());[T(M,u,r[q],{q:u*S[q][0]}|o)for q in Q if q not in o and(u:=t-Q[q])>0]
M={};T(M,26);E={(*sorted(n),):M[n]for n in sorted(M,key=M.get)};T(M,30)
print([max(M.values()),max(E[e]+E[h]for e in E for h in E if not set(h)&set(e))])
