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
    prev_pos = dict()
    prev_pos["x"] = []
    prev_pos["y"] = []
    prev_pos["z"] = []

    found = [False, False, False]

    moons = []
    for i in dat:
        s = i.split("=")
        x = int(s[1][:s[1].index(",")])
        y = int(s[2][:s[2].index(",")])
        z = int(s[3][:s[3].index(">")])
        moons.append(Moon((x,y,z)))

    x_pos = []
    y_pos = []
    z_pos = []
    for i in moons:
        x_pos.append((i.x, i.vx))
        y_pos.append((i.y, i.vy))
        z_pos.append((i.z, i.vz))

    prev_pos["x"].append(x_pos)
    prev_pos["y"].append(y_pos)
    prev_pos["z"].append(z_pos)

    for k in range(10000000):
        for i in moons:
            for j in moons:
                if i != j:
                    i.apply_vel(j)

        x_pos = []
        y_pos = []
        z_pos = []
        for i in moons:
            i.move()
            x_pos.append((i.x, i.vx))
            y_pos.append((i.y, i.vy))
            z_pos.append((i.z, i.vz))

        if x_pos not in prev_pos["x"]:
            prev_pos["x"].append(x_pos)
        elif not found[0]:
            print("X: " + str(k+1))
            found[0] = True

        if y_pos not in prev_pos["y"] :
            prev_pos["y"].append(y_pos)
        elif not found[1]:
            print("Y: " + str(k + 1))
            found[1] = True

        if z_pos not in prev_pos["z"]:
            prev_pos["x"].append(x_pos)
        elif not found[2]:
            print("Z: " + str(k + 1))
            found[2] = True

        f = False
        for i in found:
            f = f and i

        if f:
            break

    total_e = 0
    for i in moons:
        i.calc_energy()
        total_e += i.tot

    return total_e

print("1: " + str(partOne()))

def calc_axis(arr):
    vel = [0,0,0,0]

    prev_arr = copy.deepcopy(arr)
    for i in arr:
        for j in arr[]:
            if