#!/bin/bash
TIMEFORMAT=%R
for j in `seq 1 10`; do
    echo "Iteracao $j"
        for k in 7 8 9 10 11 12 13 14; do
            for i in 7 8 9 10 11 12 13 14; do
                SIZETILE=$(( 2**k ))
                SIZEVEC=$(( 2**i ))
                echo "Otimizado: $SIZEVEC - $SIZETILE"
                ( time ./loopOpt 16384 $SIZEVEC $SIZETILE ) 2>> results2d/$SIZEVEC-$SIZETILE.txt
            done
        done
     echo 'Sem otimizar'
    ( time ./loop 16384)  2>> results2d/naoOtimizado.txt
done

