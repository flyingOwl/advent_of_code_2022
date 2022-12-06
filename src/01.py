import sys
l=sorted(sum(map(int,g.split())) for g in open(sys.argv[1]).read().split("\n\n"))
print([l[-1],sum(l[-3:])])
