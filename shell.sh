REF=(324 282 260 243  80 379 293  40 306  95 116 197 116 291  67 349 69 157)
for i in ${REF[@]}
do
	echo $i
	cat ../input.txt | sed "s/IDX_REF/$i/" > inp.txt
	travis -p /Volumes/S.Russo_HDD/w/passerini/urea_cell/dfbn_04/300/lj_scaled/nvt/gro_traj/traj.gro -i inp.txt
	mv ref* $i.out
	while IFS= read -r line; do if [[ $(echo $line | grep Step) ]]; then echo $line | grep -o 'AlCl2\[[0-9]*\]' | grep -o '\[[0-9]*\]' | sed 's/\[//' | sed 's/\]//' | tr '\n' ' '; echo ""; fi;  done < $i.out > $i.log
	done
