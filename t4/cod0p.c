#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <omp.h>

int main(int argc, char *argv[]){
	int n=atoi(argv[1]),threads=atoi(argv[2]);
	float *a, *b, *c;
	a=(float*)malloc(n*sizeof(float));
	b=(float*)malloc(n*sizeof(float));
	c=(float*)malloc(n*sizeof(float));
	
	srand(time(NULL));
	#pragma omp parallel num_threads(threads)
	{
	    #pragma omp for
	    for(int i=0; i<n; i++){
		a[i]= (float)(rand()%200);
	    }
	    #pragma omp for	
	    for(int j=0; j<n; j++){
		b[j]= (float)(rand()%100);
	    }
	    #pragma omp for
	    for(int i=0; i<n; i++){
		c[i]=a[i]/0.7658+b[i]/0.3248;
	    }
	}
	
	return 0;
}
