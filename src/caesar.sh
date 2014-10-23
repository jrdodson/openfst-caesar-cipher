#! /bin/bash
# John Ryan Dodson


if [ $# -ne 2 ];
then
    echo "Usage: $0 <plaintext> <shift>"
    exit 1
fi
MAX=25

#make symbol table
./mksym.py > alpha.sym

#initial encryption
echo $2 | ./map.py | fstcompile --isymbols=alpha.sym --osymbols=alpha.sym > crypt.fsa
echo $1 | ./mkinputfst.py | fstcompile --isymbols=alpha.sym --osymbols=alpha.sym > input.fsa
fstcompose input.fsa crypt.fsa result.fsa

crypt=$(fstprint --isymbols=alpha.sym --osymbols=alpha.sym result.fsa | ./printresult.py)

echo "Ciphertext: "$crypt

#decryption loop
echo "Decrypting..."
for i in $(seq 0 $MAX); do
	echo $i | ./map.py | fstcompile --isymbols=alpha.sym --osymbols=alpha.sym > crypt.fsa
	echo $crypt | ./mkinputfst.py | fstcompile --isymbols=alpha.sym --osymbols=alpha.sym > input.fsa
	fstcompose input.fsa crypt.fsa result.fsa
	fstprint --isymbols=alpha.sym --osymbols=alpha.sym result.fsa | ./printresult.py
done
