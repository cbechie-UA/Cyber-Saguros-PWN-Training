#include <stdio.h>
#include <stdlib.h>


int vuln_func(int* hmm){
	char* name = calloc(6000,1);
	printf("\n\n%p\n\n", hmm);
	printf("Input your name:  ");
	scanf("%[^\n]", name);
	printf(name);
	free(name);
	int c;
	while((c = getc(stdin)) != '\n');
	name = calloc(100,1);
	printf("\nChange Me: \n");
	scanf("%[^\n]", name);
	printf(name);
	
	free(name);
	printf("\n\n%d\n\n", *hmm);	
	return *hmm;
}

int main(){          
	
	int changeMe = 0x00;

	if(vuln_func(&changeMe) == 0xBEEF){
		printf("\n\npwn{h0w_d1d_y0u_g3t_1n_H3r3?_l3@v3_my_b33f_@l0n3!!!}\n");
	}else{
		printf(" I don't have any beef for you.\n");
	}

	return 0;
}
