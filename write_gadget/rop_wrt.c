#include <stdio.h>
#include <stdlib.h>


char hmm[200];

void vuln_func(char* func);

int main()
{
	setbuf(stdout,(char*)0x0);
	setbuf(stdin,(char*)0x0);
	setbuf(stderr,(char*)0x0);

	vuln_func(&fgets);
	return 0;
}

void vuln_func(char* func){
	char buffer[36];
	buffer[35] = 'D';
	buffer[34] = 'C';
	buffer[33] = 'B';
	buffer[32] = 'A';

	char* shovel = calloc(100,1);
	printf("Find the treasure: ");
	scanf("%[^\n]", shovel);
	int c = 0x00;
	while((c = getc(stdin)) != '\n');
	printf(shovel);
	free(shovel);

	printf("\n\nLoad the chest: ");
	scanf("%[^\n]", &buffer[0]);	
	while((c = getc(stdin)) != '\n');

	if(buffer[35] != 'D'){
		printf("\n\nStack smashing detected goodbye!");
		exit(-1);
	}else if(buffer[34] != 'C'){
		printf("\n\nStack smashing detected goodbye!");
		exit(-1);
	}else if(buffer[33] != 'B'){
		printf("\n\nStack smashing detected goodbye!");
		exit(-1);
	}else if(buffer[32] != 'A'){
		printf("\n\nStack smashing detected goodbye!");
		exit(-1);
	}
}

void gadgets_here(){
	__asm__(
		"pop %rdi\n\t"
		"ret\n\t"
		"pop %rcx\n\t"
		"ret\n\t"	
		"pop %rax\n\t"
		"movq %rax, (%rcx)\n\t"
		"ret"
	);
}
