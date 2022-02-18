#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]){
	int n=atoi(argv[1]);
	float *a, *b, *c;
	a=(float*)malloc(n*sizeof(float));
	b=(float*)malloc(n*sizeof(float));
	c=(float*)malloc(n*sizeof(float));
	
	
	for(int i=0; i<n; i++){
		a[i]= pow(i,2)*0.464+10*i-3.789;
	}
		
	for(int j=0; j<n; j++){
		b[j]= pow(j,2)*0.5647+103*j+7.5246;
	}
	
	for(int i=0; i<n; i++){
		c[i]=(pow(a[i],2)/0.7658)+sqrt(b[i]/0.3248);
	}
	
	return 0;
}
