#include <stdio.h>
#include <stdlib.h>

void vuln_func();
char* test(int* num){

	char* name = calloc(6000,1);
	
	printf("Input your name:  ");
	scanf("%[^\n]", name);
	printf(name);

	return name;
}

int main(){          

	vuln_func();

	printf("\n\nWithout Using /proc/<pid>/maps what is fgets() address? ");
	unsigned long userInput;
	scanf("%lx", &userInput);

	long* getsAddress = &fgets;

	if(getsAddress == userInput){
                printf("\npwn{I_need_a_better_hidding_spot}\n");
        }else{
                printf("\nCan't find me?\n");
        }

	return 0;
}




void vuln_func(){
	printf("%s\n\n%lx\n\n", test(&system), &vuln_func);
}


