.text 

	Global _start

_start:
	
	; https://man7.org/linux/man-pages/man2/execve.2.html
	; char* argv[2] = {"/bin/sh", NULL}; // argv must be null terminated
	; execve("/bin/sh",argv, NULL);

	xor rdx, rdx              ; rdx is now 0x00
	mov qword rbx, "//bin/sh" ; 8 bytes to fill the register. Without // it would 
                                  ; only be 7 bytes and would introduce a random value 
                                  ; for the rbx[7]. rbx = hs/nib//

	shr rbx, 0x8              ; rbx is now hs/nib/
	push rbx                  ; Pushes "hs/nib/" onto the stack
	mov rdi, rsp              ; moves "hs/nib/" into rdi
	push rax                  ; Pushes 0x00 onto the stack (null byte)
	push rdi                  ; Pushes "hs/nib/" on to the stack
                                  ;
                                   
                                  ; Stack Frame:
                                  ; rsp 
                                  ; stack[0] = 00 = NULL
                                  ; stack[1] = 68 = h
                                  ; stack[2] = 73 = s
                                  ; stack[3] = 2f = /
                                  ; stack[4] = 6e = n
                                  ; stack[5] = 69 = i
                                  ; stack[6] = 62 = b
                                  ; stack[7] = 2f = / 
                                  ; stack[8] = 0x00 
                                  ; rbp
                                  ; rip

	mov rsi, rsp              ; Move {"/bin/sh", 0x00} into rsi 
	mov al, 0x3b              ; syscall number for execve on x86-64 linux 
	syscall                   ; The default way of entering kernel mode on x86-64 
