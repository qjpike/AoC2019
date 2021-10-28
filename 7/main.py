class IntCode:
    def __init__(self,prog, inp):
        self.prog = prog
        self.prog_ptr = 0
        self.inp = inp
        self.inp_ptr = 0

    def add_input(self,inp):
        self.inp += inp

    def get_input(self):
        self.inp_ptr += 1
        return self.inp[self.inp_ptr-1]

    def decode_opcode(self, oc):
        oc_str = str(oc)
        operand = int(oc_str[-2:])
        modes = [0, 0, 0]
        for i in range(-3,-(oc_str.__len__()+1),-1):
            modes[-i-3] = int(oc_str[i])

        return (operand,modes)

    def get_operand(self, val, mode):
        if mode == 1:
            return val
        elif mode == 0:
            return self.prog[val]
        else:
            print("Huge problem here")
            return 0

    def exec(self):

        while 1:
            op,modes = self.decode_opcode(self.prog[self.prog_ptr])
            if op == 99:
                return None
            elif op == 1:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2], modes[1])
                self.prog[self.prog[self.prog_ptr+3]] = operand1 + operand2
                self.prog_ptr += 4
            elif op == 2:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1],modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2],modes[1])
                self.prog[self.prog[self.prog_ptr+3]] = operand1*operand2
                self.prog_ptr += 4
            elif op == 3:
                self.prog[self.prog[self.prog_ptr+1]] = self.get_input()
                self.prog_ptr += 2
            elif op == 4:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                self.output = operand1
                self.prog_ptr += 2
                return self.output
            elif op == 5:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2], modes[1])
                if operand1 != 0:
                    self.prog_ptr = operand2
                else:
                    self.prog_ptr += 3
            elif op == 6:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2], modes[1])
                if operand1 == 0:
                    self.prog_ptr = operand2
                else:
                    self.prog_ptr += 3
            elif op == 7:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2], modes[1])
                if operand1 < operand2:
                    self.prog[self.prog[self.prog_ptr+3]] = 1
                else:
                    self.prog[self.prog[self.prog_ptr+3]] = 0
                self.prog_ptr += 4
            elif op == 8:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2], modes[1])
                if operand1 == operand2:
                    self.prog[self.prog[self.prog_ptr+3]] = 1
                else:
                    self.prog[self.prog[self.prog_ptr+3]] = 0
                self.prog_ptr += 4

f = open("input.txt")
dat = [int(i) for i in f.read().split(",")]

import copy
import itertools
set = [0,1,2,3,4]

inp = list(itertools.permutations(set, 5))

highest = 0
for i in inp:
    amp1 = IntCode(copy.deepcopy(dat),[i[0],0])
    amp1_o = amp1.exec()

    amp2 = IntCode(copy.deepcopy(dat),[i[1],amp1_o])
    amp2_o = amp2.exec()

    amp3 = IntCode(copy.deepcopy(dat),[i[2],amp2_o])
    amp3_o = amp3.exec()

    amp4 = IntCode(copy.deepcopy(dat),[i[3],amp3_o])
    amp4_o = amp4.exec()

    amp5 = IntCode(copy.deepcopy(dat),[i[4],amp4_o])
    amp5_o = amp5.exec()

    if amp5_o > highest:
        highest = amp5_o


print("1: " + str(highest))


set = [5,6,7,8,9]

inp = list(itertools.permutations(set, 5))

highest = 0
for i in inp:
    amp1 = IntCode(copy.deepcopy(dat),[i[0]])
    amp2 = IntCode(copy.deepcopy(dat),[i[1]])
    amp3 = IntCode(copy.deepcopy(dat),[i[2]])
    amp4 = IntCode(copy.deepcopy(dat),[i[3]])
    amp5 = IntCode(copy.deepcopy(dat),[i[4]])

    amp5_o = 0
    while True:
        amp1.add_input([amp5_o])
        amp1_o = amp1.exec()

        amp2.add_input([amp1_o])
        amp2_o = amp2.exec()

        amp3. add_input([amp2_o])
        amp3_o = amp3.exec()

        amp4.add_input([amp3_o])
        amp4_o = amp4.exec()

        amp5.add_input([amp4_o])
        amp5_o = amp5.exec()

        if amp5_o != None:
            res = amp5_o
        else:
            break

    if res > highest:
        highest = res

print("2: " + str(highest))