import copy

from IntCode import IntCode

f = open("input.txt")
dat = [int(i) for i in f.read().split(",")]


ic = IntCode(copy.deepcopy(dat),[],3)
ret = ic.exec()
field = dict()

while ret != None:

    field[(ret[0],ret[1])] = ret[2]
    ret = ic.exec()

count = 0
for i in list(field.values()):
    if i == 2:
        count += 1

print("1: " + str(count))


ic = IntCode(copy.deepcopy(dat),[],3)
ic.prog[0] = 2
field = dict()

ret = ic.exec()

points = 0
p_pos = (0,0)
b_pos = (0,0)

#used for debugging
def print_field():
    for i in range(23):
        for j in range(44):
            if field[(j, i)] == 0:
                print(" ", end="")
            elif field[(j, i)] == 1:
                print("|", end="")
            elif field[(j, i)] == 2:
                print("#", end='')
            elif field[(j, i)] == 3:
                print("_", end='')
            elif field[(j, i)] == 4:
                print("o", end='')
            else:
                print("UhOh", end='')
        print("")

    return


while ret != None:
    if ret[0] == -1:
        points = ret[2]
    else:
        field[(ret[0], ret[1])] = ret[2]

    if ret[2] == 4:
        b_pos = (ret[0],ret[1])
    elif ret[2] == 3:
        p_pos = (ret[0], ret[1])

    if b_pos[0] < p_pos[0]:
        ic.add_input([-1])
    elif b_pos[0] > p_pos[0]:
        ic.add_input([1])
    else:
        ic.add_input([0])



    # if field.__len__() == 23*44:
    #     print_field()

    ret = ic.exec()

print("2: " + str(points))

