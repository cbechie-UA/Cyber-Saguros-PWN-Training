#include <stdio.h>
#include <stdlib.h>

int main(){          
	char* name = calloc(100,1);
	
	printf("Input your name:  ");
	scanf("%[^\n]", name);
	printf("Your name is: %s\n", name);
	free(name);
	return 0;
}
