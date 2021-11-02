class IntCode:
    def __init__(self,prog, inp, o_len):
        self.prog = prog + [0]*prog.__len__()*1000
        self.prog_ptr = 0
        self.inp = inp
        self.rel_base = 0
        self.output = []
        self.output_len = o_len

    def add_input(self,inp):
        self.inp += inp

    def get_input(self):
        return self.inp[-1]

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
            print("Opcode Mode Error")
            return 0

    def get_address(self,val,mode):
        if mode == 0:
            return val
        elif mode == 2:
            return val + self.rel_base
        else:
            print("Addressing Error")

    def exec(self):

        while 1:
            op,modes = self.decode_opcode(self.prog[self.prog_ptr])

            if op == 99:
                return None
            elif op == 1:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2], modes[1])
                self.prog[self.get_address(self.prog[self.prog_ptr+3],modes[2])] = operand1 + operand2
                self.prog_ptr += 4
            elif op == 2:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1],modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2],modes[1])
                self.prog[self.get_address(self.prog[self.prog_ptr+3],modes[2])] = operand1*operand2
                self.prog_ptr += 4
            elif op == 3:
                self.prog[self.get_address(self.prog[self.prog_ptr+1],modes[0])] = self.get_input()
                self.prog_ptr += 2
            elif op == 4:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                self.output += [operand1]
                self.prog_ptr += 2
                if self.output.__len__() == self.output_len:
                    r = self.output[-(self.output_len):]
                    self.output = []
                    return r
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
                    self.prog[self.get_address(self.prog[self.prog_ptr+3],modes[2])] = 1
                else:
                    self.prog[self.get_address(self.prog[self.prog_ptr+3],modes[2])] = 0
                self.prog_ptr += 4
            elif op == 8:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                operand2 = self.get_operand(self.prog[self.prog_ptr+2], modes[1])
                if operand1 == operand2:
                    self.prog[self.get_address(self.prog[self.prog_ptr+3],modes[2])] = 1
                else:
                    self.prog[self.get_address(self.prog[self.prog_ptr+3],modes[2])] = 0
                self.prog_ptr += 4
            elif op == 9:
                operand1 = self.get_operand(self.prog[self.prog_ptr+1], modes[0])
                self.rel_base += operand1
                self.prog_ptr += 2
            else:
                print("Op Code Error: OpCode = " + str(op) + ", ProgPtr = " + str(self.prog_ptr))
                return None