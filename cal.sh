#!/bin/bash

read num1 < num1.txt
read num2 < num2.txt

if [ $# -lt 1 ] ; then
	# no parameter
     echo "...none operator parameter..."
     PS3='select menu : '

     select num in add sub div mul
     do
		set $num
		break
     done
fi

echo "num1 : $num1"
echo "num2 : $num2"
echo "op : $1"

case $1 in
	add) let result=$(($num1 + $num2));;
	sub) let result=$(($num1 - $num2));;
	div) let result=$(($num1 / $num2));;
	mul) let result=$(($num1 * $num2));;
esac

echo "result : $result"
