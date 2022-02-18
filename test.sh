#!/bin/bash
TIMEFORMAT=%R
for l in 5 6 7 8; do
    echo "Diretorio $l"
    for j in `seq 1 30`; do
    	bash -c 'echo 1 > /proc/sys/vm/drop_caches'
        echo "Iteracao $j"
	for i in 6 7 8 9 10 11 12 13 14 15; do
	    N=$(( i*10**5 ))
	    for k in 10 11 12 13 14 15 16 17 18 19; do
		STRIP=$(( 2**k ))
		echo "Otimizado: $N - $STRIP"
		( time ./cod$l $N $STRIP ) 2>> results/results$l/$N-$STRIP.txt
	    done
	done
    done
    for j in `seq 1 5`; do
        bash -c 'echo 1 > /proc/sys/vm/drop_caches'
        for i in 6 7 8 9 10 11 12 13 14 15 ;do
    	    N=$(( i*10**5 ))
	    echo 'Sem otimizar'
	    ( time ./cod1 $N)  2>> results/results$l/naoOtimizado1$N.txt
	    bash -c 'echo 1 > /proc/sys/vm/drop_caches'
	    ( time ./cod2 $N)  2>> results/results$l/naoOtimizado2$N.txt
	    bash -c 'echo 1 > /proc/sys/vm/drop_caches'
	    ( time ./cod3 $N)  2>> results/results$l/naoOtimizado3$N.txt
	    bash -c 'echo 1 > /proc/sys/vm/drop_caches'
	    ( time ./cod4 $N)  2>> results/results$l/naoOtimizado4$N.txt
  	    bash -c 'echo 1 > /proc/sys/vm/drop_caches'
        done
    done
done

find ./results/ -type f -name "*.txt" | xargs -L1 sed -i 's/,/./g'

