#include <stdio.h>

void ret2win(){
	printf("PWN{s1mpl3_buff3r_0vrfl0w_D3M0}");
}

void vuln_function();

int main(){
	vuln_function();	
	return 0;
}

void vuln_function(){
	char buffer[8] = {'\0'};
	gets(buffer);
}
