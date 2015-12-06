f = open('input03_01', 'r')
print f
arrows = f.read()
print arrows
x = 0
y = 0
visitedplaces = [(0,0)]
presents = 1
for letter in arrows:
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
print visitedplaces

print presents
