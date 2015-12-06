f = open('input02_01', 'r')
print f
dimens = f.read()
lines = dimens.split('\n')
totalrib = 0
for line in lines:
    threenumbers = line.split('x')
    print threenumbers
    if len(threenumbers) > 1:
        edge0 = int(threenumbers[0])
        edge1 = int(threenumbers[1])
        edge2 = int(threenumbers[2])
        perim0 = 2 * (edge1 + edge2)
        perim1 = 2 * (edge0 + edge2)
        perim2 = 2 * (edge0 + edge1)
        print perim0, perim1, perim2, edge0 * edge1 * edge2
        totalrib += min(perim0, perim1, perim2)
        totalrib += edge0 * edge1 * edge2
print totalrib
