#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]){
	
	int n=atoi(argv[1]), VECLEN=atoi(argv[2]), TILE=atoi(argv[3]);
	float *a, *b, *matriz;
	a=(float*)malloc(n*sizeof(float));
	b=(float*)malloc(n*sizeof(float));
	matriz=(float*)malloc(n*n*sizeof(float));
	
	srand(time(NULL));
	
	for(int i=0; i<n; i++){
		a[i]= (float)(rand()%200);
	}
		
	for(int j=0; j<n; j++){
		b[j]= (float)(rand()%100);
	}
	
	for(int ii=0; ii<n; ii+=TILE){
		for(int i=ii; i<ii+TILE; i++){
			for(int jj=0; jj<n; jj+=VECLEN){
				for(int j=jj; j<jj+VECLEN; j++){
					matriz[i*n+j]=a[i]*b[j];
				}
			}
		}
	}
	
	return 0;
}
