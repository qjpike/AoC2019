f = open("input.txt")
dat = f.read().strip()

w = 25
h = 6

layers = []

for i in range(0,len(dat),w*h):
    layers.append(dat[i:i+w*h])

fewest = 9999
curr = ''
for i in layers:
    if i.count('0') < fewest:
        fewest = i.count('0')
        curr = i

print("1: " + str(curr.count('1')*curr.count('2')))

image = ['2' for i in range(w*h)]

for i in layers:
    for j in range(w*h):
        if image[j] == '2':
            if i[j] != '2':
                image[j] = i[j]

for i in range(h):
    for j in range(w):
        if image[i*w+j] == '0':
            print(" ",end='')
        else:
            print("#",end='')
    print("")

