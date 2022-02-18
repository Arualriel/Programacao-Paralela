#!/bin/bash

module load gcc/10.2

gcc -O3 -fopt-info-vec-all cod80_gpu.c -o cod80_gpu -lm
gcc -O3 -fopt-info-vec-all cod0_gpu.c -o cod0_gpu -lm
gcc -O3 -fopt-info-vec-all cod0.c -o cod0 -lm
gcc -O3 -fopt-info-vec-all cod80.c -o cod80 -lm
gcc -fopenmp -O3 -fopt-info-vec-all cod84.c -o cod84 -lm

chmod +x testsd.sh
chmod +x testsd-gpu.sh
chmod +x submetersd.sh
chmod +x submetersd-gpu.sh
echo '*** COMPILACAO COMPLETADA ***'

