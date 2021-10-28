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
                    v = ('a_up',10000000)
                else:
                    v = ('e_down',-10000000)
            elif target[1] == asteroid[1]:
                if target[0] < asteroid[0]:
                    v = ('g_left', 0)
                else:
                    v = ('c_right', 0)
            else:
                m = (asteroid[1] - target[1]) / (asteroid[0] - target[0])
                if asteroid[1] < target[1]:
                    v = ("h1",m)
                else:
                    v = ("h2",m)
            if v in slopes:
                slopes[v] += [target]
            else:
                slopes[v] = [target]

    if slopes.__len__() > max:
        pick = asteroid
        pick_slopes = slopes
        max = slopes.__len__()

print("1: " + str(max) + " " + str(pick))

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
print(slopes_raw.sort())

# put the asteroids in order of destruction

# find the asteroid at position 200


