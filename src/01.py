import sys
d=[[int(i) for i in g.split()] for g in open(sys.argv[1]).read().split("\n\n")]
l=sorted(map(sum,d))[-3:]
print([l[-1],sum(l)])
