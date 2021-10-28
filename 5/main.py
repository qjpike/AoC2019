class IntCode:
    def __init__(self,prog):
        self.prog = prog
        self.prog_ptr = 0

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
                return
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
                self.prog[self.prog[self.prog_ptr+1]] = int(input("Input Value: "))
                self.prog_ptr += 2
            elif op == 4:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                print("Output: " + str(operand1))
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
inp = f.read().split(",")
dat = [int(i) for i in inp]


ic = IntCode(dat)
print("1: " + str(ic.exec()))





















#----------------------------------------------------------#
# Day 2 code for testing
#----------------------------------------------------------#
# f = open("input.txt")
# inp = f.read().split(",")
# dat = [int(i) for i in inp]
#
# dat[1] = 12
# dat[2] = 2
#
# ic = IntCode(dat)
# print("1: " + str(ic.exec()))
#
# for i in range(99):
#     for j in range(99):
#         dat = [int(i) for i in inp]
#         dat[1] = i
#         dat[2] = j
#         ic = IntCode(dat)
#         if ic.exec() == 19690720:
#             print("2: " + str(100*i + j))
#             break
#
