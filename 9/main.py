class IntCode:
    def __init__(self,prog, inp):
        self.prog = prog + [0]*prog.__len__()*10
        self.prog_ptr = 0
        self.inp = inp
        self.inp_ptr = 0
        self.rel_base = 0
        self.output = []

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
        elif mode == 2:
            return self.prog[val + self.rel_base]
        else:
            print("Huge problem here")
            return 0

    def exec(self):

        while 1:
            op,modes = self.decode_opcode(self.prog[self.prog_ptr])

            if op == 99:
                return self.output
            elif op == 1:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2], modes[1])
                rel = 0
                if modes[2] == 2:
                    rel = self.rel_base
                self.prog[self.prog[self.prog_ptr+3] + rel] = operand1 + operand2
                self.prog_ptr += 4
            elif op == 2:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1],modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2],modes[1])
                rel = 0
                if modes[2] == 2:
                    rel = self.rel_base
                self.prog[self.prog[self.prog_ptr+3]+rel] = operand1*operand2
                self.prog_ptr += 4
            elif op == 3:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1],modes[0])
                if modes[0] == 2:
                    operand1 = self.rel_base + self.prog[self.prog_ptr+1]
                self.prog[operand1] = self.get_input()
                self.prog_ptr += 2
            elif op == 4:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                self.output += [operand1]
                self.prog_ptr += 2
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
                rel = 0
                if modes[2] == 2:
                    rel = self.rel_base
                if operand1 < operand2:
                    self.prog[self.prog[self.prog_ptr+3]+rel] = 1
                else:
                    self.prog[self.prog[self.prog_ptr+3]+rel] = 0
                self.prog_ptr += 4
            elif op == 8:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2], modes[1])
                rel = 0
                if modes[2] == 2:
                    rel = self.rel_base
                if operand1 == operand2:
                    self.prog[self.prog[self.prog_ptr+3]+rel] = 1
                else:
                    self.prog[self.prog[self.prog_ptr+3]+rel] = 0
                self.prog_ptr += 4
            elif op == 9:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                self.rel_base += operand1
                self.prog_ptr += 2

f = open("input.txt")
dat = [int(i) for i in f.read().strip().split(",")]

print(dat)
import copy
ic = IntCode(copy.deepcopy(dat),[1])
print("1: " + str(ic.exec()[0]))

ic2 = IntCode(copy.deepcopy(dat),[2])
print("2: " + str(ic2.exec()[0]))