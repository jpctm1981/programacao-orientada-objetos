#include <stdio.h>
#include <stdlib.h>

int main(){

	int a, fat;

	printf("informe um número para cálculo do fatorial:  ");
	scanf("%d", &a);

	for(fat = 1; a > 1; a = a - 1){
		fat=fat*a;
	}

	printf("\nFatorial = %d\n ", fat );

return 0;

}


// joao@joao-Aspire-E5-574:~/POO$ gcc fatorial.c -o fatorial
//joao@joao-Aspire-E5-574:~/POO$ ./fatorial
