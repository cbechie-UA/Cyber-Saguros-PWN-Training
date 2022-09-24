#include <stdio.h>
#include <stdlib.h>

int main(){          
	unsigned long* getsAddress = &fgets;

	unsigned long userInput = 0x00;
	printf("Find fgets() address using /proc/<pid>/maps \n");
	printf("\nWhat is fgets() address? ");
	scanf("%lx", &userInput);

	if(getsAddress == userInput){
		printf("\npwn{You_Found_Me!}\n");
	}else{
		printf("\nI'm lost can you find me?\n");
	}

	return 0;
}
