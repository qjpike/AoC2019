from math import ceil

f = open("input.txt")
lines = [i.strip() for i in f.readlines()]

formulas = dict()
for k in lines:
    in_out = k.split("=>")

    ins_str = in_out[0].split(",")
    outs_str = in_out[1]

    ins_tups = []
    outs_tups = []
    for i in ins_str:
        l = i.strip().split(" ")
        ins_tups.append((int(l[0]),l[1]))

    l = outs_str.strip().split(" ")
    outs_tups = ( int(l[0]), l[1])

    formulas[outs_tups[1]] = (outs_tups[0], ins_tups)

form = formulas['FUEL'][1]

remaining = dict()


# Steps:
# 1. Pop off the first element.
# 2. If there are already enough of that element in remaining:
#       - subtract the values from remaining
#       - throw away the element
#   if there are not already enough of that element in remaining:
#       - add that element's formula to the end of the total formula
#       - add the number of elements created to remaining
#       - loop back to start of step 2
# 3. consolidate the formula
# 4. repeat 1 - 3 until only ORE exists in the formula
def create_element(interested, needed, remaining):
    have = remaining[interested]
    more = needed - have
    mult = ceil(more/formulas[interested][0])
    rem = have + mult*formulas[interested][0] - needed
    remaining[interested] = rem
    return [(i*mult,el) for i,el in formulas[interested][1]]

def consolidate_formula(form):
    vals = dict()
    for i in form:
        if i[1] in vals:
            vals[i[1]] += i[0]
        else:
            vals[i[1]] = i[0]

    return [(vals[i],i) for i in list(vals.keys())]

# while True:
#     interested = form.pop(0)
#     if interested[1] == "ORE":
#         if len(form) == 0:
#             form = interested
#             break
#         else:
#             form.append(interested)
#     elif interested[1] in remaining \
#             and interested[0] < remaining[interested[1]]:
#         remaining[interested[1]] -= interested[0]
#     elif interested[1] not in remaining:
#         remaining[interested[1]] = 0
#         form += create_element(interested[1], interested[0])
#         form = consolidate_formula(form)
#     else:
#         form += create_element(interested[1], interested[0])
#         form = consolidate_formula(form)



def calc_fuel_needed(mult):
    form = [(i*mult,el) for i,el in formulas['FUEL'][1]]
    remaining = dict()
    while True:
        interested = form.pop(0)
        if interested[1] == "ORE":
            if len(form) == 0:
                form = interested
                break
            else:
                form.append(interested)
        elif interested[1] in remaining \
                and interested[0] < remaining[interested[1]]:
            remaining[interested[1]] -= interested[0]
        elif interested[1] not in remaining:
            remaining[interested[1]] = 0
            form += create_element(interested[1], interested[0], remaining)
            form = consolidate_formula(form)
        else:
            form += create_element(interested[1], interested[0], remaining)
            form = consolidate_formula(form)

    return form[0]


print("1: ", calc_fuel_needed(1))

for i in range(12039400,12039500):
    z = calc_fuel_needed(i)
    if z > 1000000000000:
        break

print("2: ",i-1)