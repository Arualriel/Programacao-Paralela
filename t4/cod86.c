#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

int main(int argc, char *argv[]){
    int n=atoi(argv[1]), STRIP=atoi(argv[2]), threads=atoi(argv[3]);
    int nPrime=n-n%STRIP;
    float *a, *b, *c;
    a=(float*)malloc(n*sizeof(float));
    b=(float*)malloc(n*sizeof(float));
    c=(float*)malloc(n*sizeof(float));
    float ca=1/0.7658, cb=1/0.3248;
    #pragma omp parallel num_threads(threads)
    { 
	#pragma omp simd
	for(int j=0; j<n; j++){
	    a[j]= pow(j,2)*0.464+10*j-3.789;
	    b[j]= pow(j,2)*0.5647+103*j+7.5246;
	}
	#pragma omp for schedule(dynamic)
	for(int ii=0; ii<nPrime; ii+=STRIP){
	    #pragma omp simd
	    for(int i=ii; i<ii+STRIP; i++){
	        c[i]=a[i]*ca+b[i]*cb;
 	    }
	}    
	#pragma omp simd 
	for(int j=nPrime;j<n;j++){
	    c[j]=(pow(a[j],2)*ca)+sqrt(b[j]*cb);	               
	}
    }
    return 0;
}
