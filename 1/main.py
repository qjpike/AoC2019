f = open("input.txt")
dat = f.readlines()

fuel = 0
for i in dat:
    fuel += (int(i)//3) - 2

print("1: " + str(fuel))

fuel = 0
for i in dat:
    add = (int(i)//3)-2
    fuel += add
    while add > 8:
        add = add//3 - 2
        fuel += add

print(fuel)
