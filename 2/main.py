class IntCode:
    def __init__(self,prog):
        self.prog = prog
        self.prog_ptr = 0

    def exec(self):
        while 1:
            if self.prog[self.prog_ptr] == 99:
                return self.prog[0]
            elif self.prog[self.prog_ptr] == 1:
                self.prog[self.prog[self.prog_ptr+3]] = self.prog[self.prog[self.prog_ptr + 1]] + self.prog[self.prog[self.prog_ptr + 2]]
                self.prog_ptr += 4
            elif self.prog[self.prog_ptr] == 2:
                self.prog[self.prog[self.prog_ptr+3]] = self.prog[self.prog[self.prog_ptr + 1]] * self.prog[self.prog[self.prog_ptr + 2]]
                self.prog_ptr += 4

f = open("input.txt")
inp = f.read().split(",")
dat = [int(i) for i in inp]

dat[1] = 12
dat[2] = 2

ic = IntCode(dat)
print("1: " + str(ic.exec()))

for i in range(99):
    for j in range(99):
        dat = [int(i) for i in inp]
        dat[1] = i
        dat[2] = j
        ic = IntCode(dat)
        if ic.exec() == 19690720:
            print("2: " + str(100*i + j))
            break