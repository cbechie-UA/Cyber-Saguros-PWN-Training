#include <stdio.h>
#include <stdlib.h>


void vuln_func(char* buffer){
	printf("Crack some eggs at %p\n", buffer);
	gets(buffer);	

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
	
	char buffer[36];
	buffer[35] = 'D';
	buffer[34] = 'C';
	buffer[33] = 'B';
	buffer[32] = 'A';	
		
	char* pBuffer = &buffer[0];

	vuln_func(pBuffer);

	printf("\n\nReturned from vuln func\n");

	return 0;
}
