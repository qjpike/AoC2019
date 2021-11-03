from IntCode import IntCode

f = open("input.txt")
dat = [int(i.strip()) for i in f.read().split(",")]

ic = IntCode(dat,[],1)

curr_x = 0
curr_y = 0

move_arr = [1,2,3,4]
next_arr = [(0,1), (0,-1), (1,0), (-1,0)]


field = dict()
field[(curr_x, curr_y)] = 3


def print_field(curr):
    minx = 100000
    miny = 100000
    maxx = -100000
    maxy = -100000
    for i in list(field.keys()):
        if i[0] < minx: minx = i[0]
        elif i[0] > maxx: maxx = i[0]
        if i[1] < miny: miny = i[1]
        if i[1] > maxy: maxy = i[1]

    for i in range(maxy+1,miny-1,-1):
        for j in range(minx-1,maxx+1):
            if (j,i) == curr:
                print("^",end='')
            elif (j,i) in field:
                if field[(j,i)] == 0:
                    print("#",end='')
                elif field[(j,i)] == 1:
                    print(".",end='')
                elif field[(j,i)] == 2:
                    print("O",end='')
                elif field[(j,i)] == 3:
                    print("S",end='')
            else:
                print(" ",end='')
        print("")

#this can be used to manually search the maze
while True:
    n = input("Next: ")
    if n < "9" and n > "0":
        n = int(n)
    if n in move_arr:
        ic.add_input([n])
        res = ic.exec()
        next_x = curr_x + next_arr[move_arr.index(n)][0]
        next_y = curr_y + next_arr[move_arr.index(n)][1]
        field[(next_x,next_y)] = res[0]
        if res[0] == 1 or res[0] == 2:
            curr_y = next_y
            curr_x = next_x
        print_field((curr_x,curr_y))

# to answer step 1, I created the full maze, now in map.txt, and drew the path as commas. There
#   are 411 commas + 1 step for the O sensor. Answer = 412
# to answer step 2, I took map.txt, added commas between each character, and imported it into
#   an excel file, map.xlsx. Then, stepping back by one from the O, you can count out the
#   longest path. two boxes are highlighted where I made a 1-off error. longest path is 319.
#   Answer = 418