#!/bin/bash
TIMEFORMAT=%R
for j in `seq 1 30`; do
    echo "0 - Iteracao $j"
    ( time ./cod0_gpu 80000 ) 2>> results-gpu/results0/8.txt
    ( time ./cod0_gpu 90000 ) 2>> results-gpu/results0/9.txt
    ( time ./cod0_gpu 100000 ) 2>> results-gpu/results0/10.txt
    ( time ./cod0_gpu 110000 ) 2>> results-gpu/results0/11.txt
    ( time ./cod0_gpu 120000 ) 2>> results-gpu/results0/12.txt
    ( time ./cod0_gpu 130000 ) 2>> results-gpu/results0/13.txt
    ( time ./cod0_gpu 140000 ) 2>> results-gpu/results0/14.txt
    ( time ./cod0_gpu 150000 ) 2>> results-gpu/results0/15.txt
    ( time ./cod0_gpu 160000 ) 2>> results-gpu/results0/16.txt
    ( time ./cod0_gpu 170000 ) 2>> results-gpu/results0/17.txt
done
	    

for i in `seq 1 30`; do
    echo "SM - Iteracao $j"
    ( time ./cod80_gpu 80000 2048 )  2>> results-gpu/results80/8.txt
    ( time ./cod80_gpu 90000 65536 )  2>> results-gpu/results80/9.txt
    ( time ./cod80_gpu 100000 16384 )  2>> results-gpu/results80/10.txt
    ( time ./cod80_gpu 110000 512 )  2>> results-gpu/results80/11.txt
    ( time ./cod80_gpu 120000 4096 )  2>> results-gpu/results80/12.txt
    ( time ./cod80_gpu 130000 1024 )  2>> results-gpu/results80/13.txt
    ( time ./cod80_gpu 140000 8192 )  2>> results-gpu/results80/14.txt
    ( time ./cod80_gpu 150000 2048 )  2>> results-gpu/results80/15.txt
    ( time ./cod80_gpu 160000 1024 )  2>> results-gpu/results80/16.txt
    ( time ./cod80_gpu 170000 1024 )  2>> results-gpu/results80/17.txt
done

find ./results-gpu/ -type f -name "*.txt" | xargs -L1 sed -i 's/,/./g'

