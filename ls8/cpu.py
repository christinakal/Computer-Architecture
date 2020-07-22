"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0  # program counter
        self.reg = [0] * 8 # multiply by how many registers

    def load(self):
        """Load a program into memory."""

        address = 0

        program = []
        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    program.append(line)
            print(1) # is this like print(true)?

        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found!")
            sys.exit(2) # what this means?

        if program is None:
            print("No program specified!")
            return
        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    # ADD ram_read AND ram_write FUNCTIONS
 
    def ram_read(self, address=None):
        value = self.ram[address]
        return value
    
    def ram_write(self, value=None, address=None):
        self.ram[address] = value

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

    # IMPLEMENT THIS -->
    def run(self):
        """Run the CPU."""
        running = True
        
        while running:
            # IR -> Instruction Register, stores the memory address
            instruction = self.ram_read(self.pc)
            # Using ram_read(), read the bytes at PC+1 and PC+2 from RAM into variables operand_a and operand_b in case the instruction needs them.
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if instruction == 0b10000010:  # from LDI instruction
                self.reg[operand_a] = operand_b
                self.pc += 3
            elif instruction == 0b01000111:  # from PRN instruction
                print(self.reg[operand_a])
                self.pc += 2
            elif instruction == 0b00000001: # HALT (HLT)
                running = False



