

f = open("input.txt")
i = f.readlines()

l0 = i[0].split(",")
l1 = i[1].split(",")

l0pos = (0,0)
l1pos = (0,0)

l0_all_pos = [(0,0)]
l1_all_pos = [(0,0)]

for j in l0:
    if j[0] == "R":
       for k in range(int(j[1:])):
           l0pos = (l0pos[0]+1,l0pos[1])
           l0_all_pos.append(l0pos)
    elif j[0] == "L":
       for k in range(int(j[1:])):
           l0pos = (l0pos[0]-1,l0pos[1])
           l0_all_pos.append(l0pos)
    elif j[0] == "U":
       for k in range(int(j[1:])):
           l0pos = (l0pos[0],l0pos[1]+1)
           l0_all_pos.append(l0pos)
    elif j[0] == "D":
       for k in range(int(j[1:])):
           l0pos = (l0pos[0],l0pos[1]-1)
           l0_all_pos.append(l0pos)

for j in l1:
    if j[0] == "R":
       for k in range(int(j[1:])):
           l1pos = (l1pos[0]+1,l1pos[1])
           l1_all_pos.append(l1pos)
    elif j[0] == "L":
       for k in range(int(j[1:])):
           l1pos = (l1pos[0]-1,l1pos[1])
           l1_all_pos.append(l1pos)
    elif j[0] == "U":
       for k in range(int(j[1:])):
           l1pos = (l1pos[0],l1pos[1]+1)
           l1_all_pos.append(l1pos)
    elif j[0] == "D":
       for k in range(int(j[1:])):
           l1pos = (l1pos[0],l1pos[1]-1)
           l1_all_pos.append(l1pos)


intersections = set(l0_all_pos).intersection(set(l1_all_pos))

dist = 999999999
closest = (0,0)
tot_steps = 999999999999

for i in intersections:
    curr_dist = abs(i[0]) + abs(i[1])
    if curr_dist != 0 and curr_dist < dist:
        closest = i
        dist = curr_dist
    curr_total = l0_all_pos.index(i) + l1_all_pos.index(i)
    if curr_total != 0 and curr_total < tot_steps:
        tot_steps = curr_total

print("1: " + str(dist))
print("2: " + str(tot_steps))