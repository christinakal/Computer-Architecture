Transistors - the most basic - A transistor is a semiconductor device (electronic component) used to amplify or switch electronic signals and electrical power. It is composed of semiconductor material useally with at least three terminals for connection in an external circuit.
Gates - made from transistors - understands boolean logic
Digital logic
Gates can be put together into more complex structures like ... CPUs

CPU ->  brain of the computer, executes instructions
        Registers -> they can store words that can be acessed in ultra high speed because it's inside the cpu unlike RAM which is farthest
        Think of them as variables
        Stored directly on the cpu
        CPU keeps track of the address of the currently executing instruction in RAM and performs different actions based on the unstruction found there
        The address of the currently-executing instruction is held in a special register called the program counter PC
        CPUs usually have a significant amount of instructions, usually aroung 50-200
CPU Clock ->in a modern cpu triggers a few billion times per second
            clock cycle rate is measured in Hz or GHz
            each instuction takes 1 cycle or more to execute
            the faster the clock the more instructions can execute per second
ALU ->it does the arithmetic operations
        what makes CPU faster-> duplkicate hardware components
        multi-core CPUs
        pipelining
        timesharing
System Bus -> how the data is passed from CPU to RAM and from CPU to the peripherals

RAM -> Stands for Random Access Memory
        It's fast compared to hard drives and SSDs - Big array of bytes that you can access by index
        Each element in RAM can store one byte, an 8-bit number, larger muti-byte values are stored in a sequencial address in RAM
        Bytes of data are stored in RAM

        Larger 64bit (8-byte) numbers, stored sequentially in RAM, that the CPU can operate on at once are called words -> the exact number of bytes per word depends on the architecture
        - 8 bytes for a 64-bit CPU
        - 4 bytes for a 32-bit CPU
        - 1 byte fot a 8-bit CPU

    for example: if a CPU has to do a math operation, to add 2 numbers together. It is able to add 2 64-bit numbers at once if it is a 64-bit computer

        caching: it's slow to take data from RAM but access to registers is faster

CHALLENGE: <-- Answer these over the weekend

- How long does it take the number of transistors on a CPU to double? What is the common name for this rule of thumb?
- Why are registers necessary? Why not just use RAM?
- Why is cache useful?
- What is a CPU word?
- What is the system bus and how wide is it?
- Describe the pins that are on a CPU chips
- What is a CPU instruction?
