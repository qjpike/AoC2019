

f = open("input.txt")
dat = f.readlines()

def shuffle(d_size,target_card):
    for i in dat:
        i.strip()
        if i.startswith("deal into new stack"):
            if target_card <= d_size/2:
                target_card = d_size - target_card - 1
            else:
                target_card = d_size - target_card -1

        elif i.startswith("deal with increment"):
            j = int(i[20:].strip())
            target_card = (target_card*j)%d_size

        elif i.startswith("cut"):
            j = int(i[4:].strip())
            target_card -= j
            if target_card < 0:
                target_card = d_size + target_card
            elif target_card > d_size:
                target_card -= d_size
    return target_card

print("1: " + str(shuffle(10007,2019)))

card_count = 119315717514047
shuffle_count = 101741582076661

def c_c(cmd1, cmd2):
    cmdr = []
    cmdr.append(("c",(cmd1[1]+cmd2[1])%card_count))
    return cmdr

def di_di(cmd1, cmd2):
    cmdr = []
    cmdr.append(("di",(cmd1[1]*cmd2[1])%card_count))
    return cmdr

def dn_dn(cmd1,cmd2):
    cmdr = []
    return cmdr

def c_di(cmd1, cmd2):
    cmdr = []
    cmdr.append(("di",cmd2[1]))
    cmdr.append(("c",(cmd1[1]*cmd2[1])%card_count))
    return cmdr

def dn_di(cmd1,cmd2):
    cmdr = []
    cmdr.append(("di",cmd2[1]))
    cmdr.append(("c",-(cmd2[1]-1)))
    cmdr.append(("dn",0))
    return cmdr

def c_dn(cmd1,cmd2):
    cmdr = []
    cmdr.append(("dn",0))
    cmdr.append(("c",(card_count - cmd1[1])%card_count))
    return cmdr

cmds = []

for l in dat:
    l.strip()
    if l.startswith("cut"):
        cmds.append(("c",int(l[4:].strip())))
    elif l.startswith("deal with increment"):
        cmds.append(("di",int(l[20:].strip())))
    elif l.startswith("deal into"):
        cmds.append(("dn",0))

cmds.reverse()

def condense_shuffle(cmds):
    while cmds.__len__() > 3:
        i = 0
        new_cmds = []

        while i < cmds.__len__() - 1:

            if cmds[i][0] == cmds[i+1][0]:
                if cmds[i][0] == "c":
                    new_cmds += c_c(cmds[i],cmds[i+1])
                    i += 1
                elif cmds[i][0] == "di":
                    new_cmds += di_di(cmds[i],cmds[i+1])
                    i += 1
                elif cmds[i][0] == "dn":
                    new_cmds += dn_dn(cmds[i],cmds[i+1])
                    i += 1
            else:
                new_cmds.append(cmds[i])
            i += 1

        new_cmds += cmds[i:]
        cmds = new_cmds

        i = 0
        new_cmds = []
        while i < cmds.__len__()-1:
            if cmds[i][0] == "c" and cmds[i+1][0] == "di":
                new_cmds += c_di(cmds[i],cmds[i+1])
                i += 1
            elif cmds[i][0] == "dn" and cmds[i+1][0] == "di":
                new_cmds += dn_di(cmds[i],cmds[i+1])
                i += 1
            elif cmds[i][0] == "c" and cmds[i+1][0] == "dn":
                new_cmds += c_dn(cmds[i],cmds[i+1])
                i += 1
            else:
                new_cmds.append(cmds[i])
            i += 1

        new_cmds += cmds[i:]
        cmds = new_cmds

    return cmds


# cmds_condensed = condense_shuffle(cmds)
# # one shuffle is ('di', 15389743563730), ('c', -3362), ('c', 95137568973729)
# # with the input shuffle reversed.
# cmds = []
# cmds += cmds_condensed
#
# remaining = shuffle_count
# for i in range(5):
#     cmds *= 500
#     cmds = condense_shuffle(cmds)
# remaining -= 500**5
# print(remaining)
#
# final_cmds = []
# final_cmds += (cmds)


m = 119315717514047
n = 101741582076661
pos = 2020
shuffles = {'deal with increment': lambda x,m,a,b: (a*x%m,b*x%m),
            'deal into new stack': lambda _,m,a,b: (-a%m,(m-1-b)%m),
            'cut':lambda x,m,a,b:(a,(b-x)%m)}
a,b = 1,0
with open("input.txt") as f:
    for s in f.read().strip().split('\n'):
        for name,fn in shuffles.items():
            if s.startswith(name):
                arg = int(s[len(name):]) if name[-1] == ' ' else 0
                a,b = fn(arg,m,a,b)
                break
r = (b*pow(1-a,m-2,m)) % m
print(f"card at #{pos}: {((pos-r)* pow(a,n*(m-2),m) + r) %m}")


m = 119315717514047
n = 101741582076661
pos = 2020
shuffles = { 'deal with increment ': lambda x,m,a,b: (a*x %m, b*x %m),
         'deal into new stack': lambda _,m,a,b: (-a %m, (m-1-b)%m),
         'cut ': lambda x,m,a,b: (a, (b-x)%m) }
a,b = 1,0
with open('input.txt') as f:
  for s in f.read().strip().split('\n'):
    for name,fn in shuffles.items():
      if s.startswith(name):
        arg = int(s[len(name):]) if name[-1] == ' ' else 0
        a,b = fn(arg, m, a, b)
        break
r = (b * pow(1-a, m-2, m)) % m
print(f"Card at #{pos}: {((pos - r) * pow(a, n*(m-2), m) + r) % m}")
