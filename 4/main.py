
min = 353096
max =  843212
count = 0
possible = []
for i in range(min,max):
    i_str = str(i)
    double = False
    for j in range(i_str.__len__()-1):
        if i_str[j] > i_str[j+1]:
            break
        if i_str[j] == i_str[j+1]:
            double = True
        if j == i_str.__len__()-2 and double == True:
            count += 1
            possible.append(i)
            break

print("1: " + str(count))

count2 = 0
for i in possible:
    i_str = str(i)
    vals = dict()
    good = False
    for j in i_str:
        if j not in vals:
            vals[j] = 1
        else:
            vals[j] += 1

    for j in list(vals.values()):
        if j == 2:
            good = True
            break

    if good:
        count2 += 1


print("2: " + str(count2))