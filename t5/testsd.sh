#!/bin/bash
TIMEFORMAT=%R
for j in `seq 1 30`; do
    echo "0 - Iteracao $j"
    ( time ./cod0 80000 ) 2>> results-ori/results0/8.txt
    ( time ./cod0 90000 ) 2>> results-ori/results0/9.txt
    ( time ./cod0 100000 ) 2>> results-ori/results0/10.txt
    ( time ./cod0 110000 ) 2>> results-ori/results0/11.txt
    ( time ./cod0 120000 ) 2>> results-ori/results0/12.txt
    ( time ./cod0 130000 ) 2>> results-ori/results0/13.txt
    ( time ./cod0 140000 ) 2>> results-ori/results0/14.txt
    ( time ./cod0 150000 ) 2>> results-ori/results0/15.txt
    ( time ./cod0 160000 ) 2>> results-ori/results0/16.txt
    ( time ./cod0 170000 ) 2>> results-ori/results0/17.txt
done	    

for i in `seq 1 30`; do
    echo "SM - Iteracao $j"
    ( time ./cod80 80000 2048 )  2>> results-ori/results80/8.txt
    ( time ./cod80 90000 65536 )  2>> results-ori/results80/9.txt
    ( time ./cod80 100000 16384 )  2>> results-ori/results80/10.txt
    ( time ./cod80 110000 512 )  2>> results-ori/results80/11.txt
    ( time ./cod80 120000 4096 )  2>> results-ori/results80/12.txt
    ( time ./cod80 130000 1024 )  2>> results-ori/results80/13.txt
    ( time ./cod80 140000 8192 )  2>> results-ori/results80/14.txt
    ( time ./cod80 150000 2048 )  2>> results-ori/results80/15.txt
    ( time ./cod80 160000 1024 )  2>> results-ori/results80/16.txt
    ( time ./cod80 170000 1024 )  2>> results-ori/results80/17.txt
done

for t in 1 2 3 4 5 6 7 8 9 10 11 12 24; do
    for j in `seq 1 30`; do
        echo "Iteracao $j"
        ( time ./cod84 80000 2048 $t ) 2>> results-oti/results84/8-$t.txt
        ( time ./cod84 90000 65536 $t ) 2>> results-oti/results84/9-$t.txt
        ( time ./cod84 100000 16384 $t ) 2>> results-oti/results84/10-$t.txt
        ( time ./cod84 110000 512 $t ) 2>> results-oti/results84/11-$t.txt
        ( time ./cod84 120000 4096 $t ) 2>> results-oti/results84/12-$t.txt
        ( time ./cod84 130000 1024 $t ) 2>> results-oti/results84/13-$t.txt
        ( time ./cod84 140000 8192 $t ) 2>> results-oti/results84/14-$t.txt
        ( time ./cod84 150000 2048 $t ) 2>> results-oti/results84/15-$t.txt
        ( time ./cod84 160000 1024 $t ) 2>> results-oti/results84/16-$t.txt
        ( time ./cod84 170000 1024 $t ) 2>> results-oti/results84/17-$t.txt
    done
done
	    



find ./results-ori/ -type f -name "*.txt" | xargs -L1 sed -i 's/,/./g'
find ./results-oti/ -type f -name "*.txt" | xargs -L1 sed -i 's/,/./g'

