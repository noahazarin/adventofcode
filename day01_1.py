f = open('input01_01','r')
print f
direction = f.read()
print direction
floor = 0
visitedB1 = False
for position, letter in enumerate(direction):
    if letter == ")":
        floor -= 1
    elif letter == "(":
        floor += 1
    if visitedB1 == False:
        print letter, position
    if floor == -1:
        if visitedB1 == False:
            print "now in -1. current position is %r"  % str(int(position)+1)
            visitedB1 = True
print floor
