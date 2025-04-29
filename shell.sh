#!/bin/bash
MAX_IDX=150
N=2
TRAJECTORY=$1

MOL1="AlCl4"
MOL2="Al2Cl7"

DELTA=$(echo $MAX_IDX'/'$N | bc)
echo 1 $DELTA $MAX_IDX 


for i in $(seq 1 $DELTA $MAX_IDX)
do
	echo $i
	cat ../input.txt | sed "s/REF_IDX/$i/" > inp.txt
	travis -p $TRAJECTORY -i inp.txt
	ls -lrt 
	mv ref* $i.out
	while IFS= read -r line; do if [[ $(echo $line | grep Step) ]]; then echo $line | grep -o "$MOL1\[[0-9]*\]" | grep -o '\[[0-9]*\]' | sed 's/\[//' | sed 's/\]//' | tr '\n' ' '; echo ""; fi;  done < $i.out > 1_$i.log
	while IFS= read -r line; do if [[ $(echo $line | grep Step) ]]; then echo $line | grep -o "$MOL2\[[0-9]*\]" | grep -o '\[[0-9]*\]' | sed 's/\[//' | sed 's/\]//' | tr '\n' ' '; echo ""; fi;  done < $i.out > 2_$i.log
	done
