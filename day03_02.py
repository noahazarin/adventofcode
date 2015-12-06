f = open('input03_01', 'r')
print f
arrows = f.read()
print arrows
x = 0
y = 0
xr = 0
yr = 0
visitedplaces = [(0,0)]
presents = 1
for index, letter in enumerate(arrows):
    if index % 2 == 0:
        #regular santa moves
        print letter
        if letter == "v":
            y -= 1
        if letter == "^":
            y += 1
        if letter == "<":
            x -= 1
        if letter == ">":
            x += 1
        thisloc = (x, y)
        if not thisloc in visitedplaces:
            presents += 1
            visitedplaces.append(thisloc)
    if index % 2 == 1:
        #robo santa moves
        print letter
        if letter == "v":
            yr -= 1
        if letter == "^":
            yr += 1
        if letter == "<":
            xr -= 1
        if letter == ">":
            xr += 1
        thisloc = (xr, yr)
        if not thisloc in visitedplaces:
            presents += 1
            visitedplaces.append(thisloc)
print visitedplaces

print presents
