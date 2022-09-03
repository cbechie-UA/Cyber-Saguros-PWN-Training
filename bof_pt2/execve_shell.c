#include <unistd.h>


int main(){

	char* argv[2] = {"/bin/sh", NULL};
	execve("/bin/sh", argv, NULL);

	return 0;
}
