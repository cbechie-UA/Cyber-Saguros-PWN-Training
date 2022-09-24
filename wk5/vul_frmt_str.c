#include <stdio.h>
#include <stdlib.h>


void vuln_func(char* junk){
	char* name = calloc(100,1);
	
	printf("Input your name:  ");
	scanf("%[^\n]", name);
	printf(name);
	
	free(name);
}

int main(){          
	vuln_func("Carl Bechie");
	printf("\nsystem() address: %p", &system );
	return 0;
}
