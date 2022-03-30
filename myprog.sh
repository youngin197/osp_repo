#!/bin/bash

#create subdirectory
echo "...create temp directory..."
mkdir temp

#copy files in temp directory
echo "...copy files to temp directory..."
cp cal.sh temp/
cp num1.txt temp/
cp num2.txt temp/

PS3='select menu : '
select num in add sub div mul
do
	echo "...$num  selected..."
	set "$num"
	break
done

echo "...run calculater..."
cd temp/
chmod 755 cal.sh
./cal.sh $num
