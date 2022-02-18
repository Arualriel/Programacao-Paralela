#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

int main(int argc, char *argv[]){
    int n=atoi(argv[1]), STRIP=atoi(argv[2]), threads=atoi(argv[3]);
    long int paddingBytes = 64;
    long int paddingElements = paddingBytes/sizeof(long int);
    long int nPadded = n + (paddingElements - n%paddingElements);
    long int nPrime=nPadded-nPadded%STRIP;
    float a=1/0.7658, b=1/0.3248;
    float a_container[threads][nPadded];
    float b_container[threads][nPadded];
    float c_container[threads][nPadded];
    #pragma omp parallel num_threads(threads)
    { 
	#pragma omp simd
	for(long int j=0; j<nPadded; j++){
	    int id=omp_get_thread_num();
	    a_container[id][j]= pow(j,2)*0.464+10*j-3.789;
	    b_container[id][j]= pow(j,2)*0.5647+103*j+7.5246;
	}
	#pragma omp for schedule(dynamic)
	for(long int ii=0; ii<nPrime; ii+=STRIP){
	    #pragma omp simd
	    for(int i=ii; i<ii+STRIP; i++){
	        int id=omp_get_thread_num();
	        c_container[id][i]=a_container[id][i]*a+b_container[id][i]*b;
 	    }
	}
	#pragma omp simd 
	for(long int j=nPrime;j<nPadded;j++){
	    int id=omp_get_thread_num();
	    c_container[id][j]=(pow(a_container[id][j],2)*a)+sqrt(b_container[id][j]*b);      
	}
    }	
    return 0;
}
