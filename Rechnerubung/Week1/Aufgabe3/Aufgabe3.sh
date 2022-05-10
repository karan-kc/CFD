#!/bin/bash

profiles=("NACA0012" "NACA2412" "NACA4412")
reynoldsNumberLimits=(2 6) #e5
reynoldsNumberStep=2	   #e5
attackAngleArray=("-5" "0" "5") #in °

for p in ${profiles[@]}; do
	for ((i=${reynoldsNumberLimits[0]}; i<=${reynoldsNumberLimits[-1]}; i+=$reynoldsNumberStep)); do
		for a in ${attackAngleArray[@]}; do
			echo "Creating folder: Parameterstudie/$p/"re"$i"e5"/"alpha"$a"
			echo -ne '>>>>>>>>>                  [33%]\r'
			sleep 0.1
			mkdir -p Parameterstudie/$p/"re"$i"e5"/"alpha"$a
			echo -ne '>>>>>>>>>>>>>>>>>>         [67%]\r'
			sleep 0.1
			touch Parameterstudie/$p/"re"$i"e5"/"alpha"$a/Vorlage
			echo -ne '>>>>>>>>>>>>>>>>>>>>>>>>>>>[100%]\r'
			sleep 0.1
		done
	done
done

echo


#mkdir -p ~/{one,two,three,four,five}/{x,y,z} Alternatively use Expansion Lists instead of loops

#touch () {
#  mkdir -p "$(dirname "$1")"
#  command touch "$1"
#}
#Alternatively, redefine the touch function to create a file within a chosen nested directory; essentialy combining mkdir and touch  

exit 0
