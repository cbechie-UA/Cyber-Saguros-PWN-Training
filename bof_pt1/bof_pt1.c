#include <stdio.h>

void ret2win(){
	printf("PWN{s1mpl3_buff3r_0vrfl0w}");
}

void vuln_function();

int main(){
	vuln_function();	
	return 0;
}

void vuln_function(){
	char buffer[32] = {'\0'};
	printf("Buffer Size: 32 bytes.\n");
	printf("Address of ret2win(): %p\n", ret2win);
	printf("Exit Here: %p \n", main + 0x14);
	gets(buffer);
}
