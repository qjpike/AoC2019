f = open("input.txt")
field = [i.strip() for i in f.readlines()]

asteroids = dict()
for i in range(field.__len__()):
    for j in range(field[i].__len__()):
        if field[i][j] == "#":
            asteroids[(j,i)] = 0

max = 0
pick = 0
for asteroid in asteroids:
    x = asteroid[0]
    y = asteroid[1]
    slopes = dict()
    for target in asteroids:
        if target != asteroid:
            if target[0] == asteroid[0]:
                if target[1] < asteroid[1]:
                    v = ('a',10000000)
                else:
                    v = ('e',-10000000)
            elif target[1] == asteroid[1]:
                if target[0] < asteroid[0]:
                    v = ('g', 0)
                else:
                    v = ('c', 0)
            else:
                m = (asteroid[1] - target[1]) / (asteroid[0] - target[0])
                if asteroid[1] < target[1]:
                    if m > 0:
                        v = ("f",m)
                    else:
                        v = ("d",m)
                else:
                    if m > 0:
                        v = ("b",m)
                    else:
                        v = ("h",m)

            if v in slopes:
                slopes[v] += [target]
            else:
                slopes[v] = [target]

    if slopes.__len__() > max:
        pick = asteroid
        pick_slopes = slopes
        max = slopes.__len__()

print("1: " + str(max))

# sort each slope's asteroids by manhattan distance
for j in list(pick_slopes.keys()):
    dists = []
    for i in pick_slopes[j]:
        dists.append((abs(i[0] - pick[0]) + abs(i[1] - pick[1]), i[0], i[1]))
    dists.sort()
    pick_slopes[j] = dists

# sort the slopes in clockwise order
slope_order = []
slopes_raw = list(pick_slopes.keys())

slopes_sorted = []
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
for i in slopes_raw:
    if i[0] == 'a':
        a.append(i)
    elif i[0] == 'b':
        b.append(i)
    elif i[0] == 'c':
        c.append(i)
    elif i[0] == 'd':
        d.append(i)
    elif i[0] == 'e':
        e.append(i)
    elif i[0] == 'f':
        f.append(i)
    elif i[0] == 'g':
        g.append(i)
    elif i[0] == 'h':
        h.append(i)

b.sort()
d.sort()
f.sort()
h.sort()

slopes_sorted = a+h+c+f+e+d+g+b


# put the asteroids in order of destruction
destroy_order = []
while destroy_order.__len__() < 250:
    for i in slopes_sorted:
        if pick_slopes[i].__len__() > 0:
            destroy_order.append(pick_slopes[i].pop(0))
        else:
            slopes_sorted.remove(i)


# find the asteroid at position 200
print("2: " + str(destroy_order[199][1]*100+destroy_order[199][2]))

