#!/bin/bash

echo "project management in github"

arr=()

read num1 < num1.txt
read num2 < num2.txt

arr+=($num1)
arr+=($num2)

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

echo "num1 : ${arr[0]}"
echo "num2 : ${arr[1]}"
echo "op : $1"

case $1 in
	add) let result=$((${arr[0]} + ${arr[1]}));;
	sub) let result=$((${arr[0]} - ${arr[1]}));;
	div) let result=$((${arr[0]} / ${arr[1]}));;
	mul) let result=$((${arr[0]} * ${arr[1]}));;
esac

echo "result : $result"
