f = open('input02_01', 'r')
print f
dimensions = f.read()
#print dimensions
lines = dimensions.split('\n')
totalpaper=0
for line in lines:
    threenumbers = line.split('x')
    print threenumbers
    if len(threenumbers) > 1:
        paperchange =0
        sides = int(threenumbers[0]) * int(threenumbers[1]) * 2
        faces = int(threenumbers[1]) * int(threenumbers[2]) * 2
        surfaces = int(threenumbers[0]) * int(threenumbers[2]) * 2
        paperchange += sides
        paperchange += faces
        paperchange += surfaces
        paperchange += min(sides, faces, surfaces)/2
        totalpaper += paperchange
print totalpaper
