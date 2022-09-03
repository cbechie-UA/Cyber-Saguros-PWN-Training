NASM_FLAGS = -f elf64 -F stabs -l 

shell_code: shell_code.o
	ld -o shell_code shell_code.o 


shell_code.o: 
	nasm $(NASM_FLAGS) shell_code.lst shell_code.asm

clean:
	rm shell_code.o
	rm shell_code.lst
	rm shell_code
	
