f = open("input.txt")
dat = [i.strip().split(")") for i in f.readlines()]

o_dict = dict()
for i in dat:
    if i[0] in o_dict:
        o_dict[i[0]] += [i[1]]
    else:
        o_dict[i[0]] = [i[1]]

def recursive_orbit_count(i, arr):

    if i in o_dict:
        tmp = o_dict[i]
        for j in tmp:
            arr += [j]
            arr.extend(recursive_orbit_count(j, []))
        o_dict[i] = arr
        return arr
    else:
        return []

recursive_orbit_count('COM', [])

count = 0
for i in list(o_dict.keys()):
    count += o_dict[i].__len__()

print("1: " + str(count))

you_loc = ''
san_loc = ''
for i in list(o_dict.keys()):
    if 'YOU' in o_dict[i]:
        you_loc = i
    if 'SAN' in o_dict[i]:
        san_loc = i
    if you_loc != '' and san_loc != '':
        break

you_back = set()
san_back = set()

for i in list(o_dict.keys()):
    if 'YOU' in o_dict[i]:
        you_back.add(i)
    if 'SAN' in o_dict[i]:
        san_back.add(i)

print("2: " + str(len(you_back - san_back) + len(san_back - you_back)))
