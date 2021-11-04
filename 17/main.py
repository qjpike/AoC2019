from IntCode import IntCode

f = open("input.txt")
dat = [int(i) for i in f.read().split(",")]

ic = IntCode(dat,[],1)
res = []


while True:
    r = ic.exec()
    if r is None:
        break
    else:
        res.append(r[0])

field = dict()

x = 0
y = 0

for i in res:

    if i == ord("#"):
        field[(x,y)] = "#"
        x += 1
    elif i == ord("."):
        field[(x,y)] = "."
        x += 1
    elif i == 10:
        x = 0
        y += 1
    elif i == ord("^"):
        field[(x,y)] = "#"
        r_pos = (x,y)
        r_or = 0
        x += 1
    elif i == ord(">"):
        field[(x,y)] = "#"
        r_pos = (x,y)
        r_or = 1
        x += 1
    elif i == ord("v"):
        field[(x,y)] = "#"
        r_pos = (x,y)
        r_or = 2
        x += 1
    elif i == ord("<"):
        field[(x,y)] = "#"
        r_pos = (x,y)
        r_or = 3
        x += 1
    else:
        print("Error at (" + str(x) + ", " + str(y) + " - Value is " + str(i))

inters = []
for i in range(1,56):
    for j in range(1,50):
        if field[(j,i)] == "#":
            if [field[(j,i-1)], field[(j+1,i)], field[(j,i+1)], field[(j-1,i)]].count("#") == 4:
                inters.append((j,i))

cal = 0
for i in inters:
    cal += i[0]*i[1]

print("1: " + str(cal))

for i in range(57):
    for j in range(51):
        print(field[(j,i)],end='')
    print("")

