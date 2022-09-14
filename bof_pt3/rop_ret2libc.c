#include <stdio.h>
#include <stdlib.h>

char* sh = "/bin/sh";

void vuln_func(){
	
	char buffer[36];
	buffer[35] = 'D';
	buffer[34] = 'C';
	buffer[33] = 'B';
	buffer[32] = 'A';	
	
	printf("What's a rop?\n");
	scanf("%s", &buffer[0]);


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

int main(){
	printf("SYSTEM: %#lx\n", &system);
	printf("Egg Shell: %#lx\n", &sh);
	vuln_func();
	return 0;
}

void gadgets(){
	__asm__(
		"pop %rdi\n\t"		
		"ret"
	);
}
