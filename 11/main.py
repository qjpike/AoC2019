from IntCode import IntCode

f = open("input.txt")
dat = [int(i) for i in f.read().strip().split(",")]

def paint(dat, inp):
    field = dict()
    r_orientation = 0 # 0 = up, 1 = right, 2 = down, 3 = left
    r_pos = (0,0)

    import copy
    ic = IntCode(copy.deepcopy(dat),[inp])


    while True:
        outp = ic.exec()
        if outp == None:
            break
        else:
            # paint
            field[r_pos] = outp[0]

            # turn
            if outp[1] == 0:
                r_orientation = (r_orientation-1)%4
            elif outp[1] == 1:
                r_orientation = (r_orientation+1)%4
            else:
                print("invalid turn")


            # step
            if r_orientation == 0:
                r_pos = (r_pos[0],r_pos[1]+1)
            elif r_orientation == 1:
                r_pos = (r_pos[0]+1,r_pos[1])
            elif r_orientation == 2:
                r_pos = (r_pos[0],r_pos[1]-1)
            elif r_orientation == 3:
                r_pos = (r_pos[0]-1,r_pos[1])
            else:
                print("invalid orientation")

            # look at panel, input back to robot
            if r_pos not in field:
                ic.add_input([0])
            else:
                ic.add_input([field[r_pos]])

    return field

print("1: " + str(paint(dat, 0).__len__()))

hull = paint(dat,1)

x_min = 111111111
x_max = -111111111

y_min = 11111111
y_max = -11111111

for i in list(hull.keys()):
    if i[0] > x_max:
        x_max = i[0]
    elif i[0] < x_min:
        x_min = i[0]

    if i[1] > y_max:
        y_max = i[1]
    elif i[1] < y_min:
        y_min = i[1]

for i in range(y_max,y_min-1,-1):
    for j in range(x_min,x_max+1):
        if (j,i) in hull:
            if hull[(j,i)]:
                print('\u2588',end='')
            else:
                print(" ",end='')
        else:
            print(" ",end='')
    print("")