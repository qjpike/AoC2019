import copy

class Moon:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.tot = 0
        self.pos = (self.x, self.y, self.z, self.vx, self.vy, self.vz)

    def __str__(self):
        s = str(("<x=" + str(self.x) + ", y=" + str(self.y) + ", z=" + str(self.z) + "> <x=" + str(self.vx) + ", y=" + str(self.vy) + ", z=" + str(self.vz) + ">"))
        return s

    def apply_vel(self,other):
        if self.x < other.x:
            self.vx += 1
        elif self.x > other.x:
            self.vx -= 1

        if self.y < other.y:
            self.vy += 1
        elif self.y > other.y:
            self.vy -= 1

        if self.z < other.z:
            self.vz += 1
        elif self.z > other.z:
            self.vz -= 1

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

        self.pos = (self.x, self.y, self.z, self.vx, self.vy, self.vz)

    def calc_energy(self):
        self.pot = abs(self.x) + abs(self.y) + abs(self.z)
        self.kin = abs(self.vx) + abs(self.vy) + abs(self.vz)
        self.tot = self.pot * self.kin


    def get_state(self):
        return((self.x, self.y, self.z, self.vx, self.vy, self.vz))

f = open("input.txt")
dat = [i.strip() for i in f.readlines()]

def partOne():
    moons = []
    for i in dat:
        s = i.split("=")
        x = int(s[1][:s[1].index(",")])
        y = int(s[2][:s[2].index(",")])
        z = int(s[3][:s[3].index(">")])
        moons.append(Moon((x,y,z)))

    for k in range(1000):
        for i in moons:
            for j in moons:
                if i != j:
                    i.apply_vel(j)

        for i in moons:
            i.move()

    total_e = 0
    for i in moons:
        i.calc_energy()
        total_e += i.tot

    return total_e

print("1: " + str(partOne()))

def calc_axis(locs):
    vels = [0,0,0,0]

    prev = []

    orgLocs = copy.deepcopy(locs)

    i = 0
    while True:


        for j in range(len(locs)):
            for k in range(len(locs)-1):
                if locs[j] < locs[(j+k+1) % len(locs)]:
                    vels[j] += 1
                elif locs[j] > locs[(j+k+1) % len(locs)]:
                    vels[j] -= 1

        for j in range(len(locs)):
            locs[j] += vels[j]

        i += 1
        if locs == orgLocs:
            i += 1
            break

    return i


xs = []
ys = []
zs = []
for i in dat:
    s = i.split("=")
    xs.append(int(s[1][:s[1].index(",")]))
    ys.append(int(s[2][:s[2].index(",")]))
    zs.append(int(s[3][:s[3].index(">")]))

x_rep = calc_axis(xs)
y_rep = calc_axis(ys)
z_rep = calc_axis(zs)

import math
lcmxy = x_rep*y_rep//math.gcd(x_rep,y_rep)
lcm = lcmxy*z_rep//math.gcd(lcmxy,z_rep)

print(x_rep,y_rep,z_rep)
print(lcm)