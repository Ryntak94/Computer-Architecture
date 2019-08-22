"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""


    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0]*256
        self.reg = [0]*8

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value

    def load(self, file):
        """Load a program into memory."""
        address = 0
        f = open(file, "r")
        for i in f:
            if i[0] == "0" or i[0] == "1":
                self.ram[address] = int("0b"+i[0:8],2)
                address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True
        PC = 0
        HALT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        while running:
            command = self.ram[PC]

            if command == LDI:
                address = self.ram[PC + 1]
                value = self.ram[PC + 2]
                PC += 3
                self.ram_write(value, address)

            elif command == PRN:
                address = self.ram[PC + 1]
                PC += 2
                print(self.ram_read(address))

            elif command == HALT:
                running = False

            else:
                print('command not recognized: {}'.format(command))
                running = False
