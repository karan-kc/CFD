#!/bin/bash

#For time file:
cat $1 | grep "Time" | sed -n 2~2p | head -n  -2 | cut -d " " -f3 > time
#Outputs 4621 lines

#For maxCourantNumber.txt file:
cat $1 | grep "Courant" | cut -d ":" -f3 > maxCourantNumber.txt

#For meanFlowVelocity.txt file:
cat $1 | grep "volAverage() of U" | cut -d "(" -f3 | cut -d " " -f1 | sed '1i\\' > meanFlowVelocity.txt

#For forcePressure.txt file:
cat $1 | grep "sum of forces" -A 1 | grep "pressure" | cut -d "(" -f2 | cut -d " " -f1 | sed '1i\\' > forcePressure.txt
#or
#cat $1 | grep -E "pressure : \(0" | cut -d "(" -f2 | cut -d " " -f1 | sed '1i\\' > forcePressure.txt

#For forceViscous.txt file:
cat $1 | grep "sum of forces" -A 2 | grep "viscous" | cut -d "(" -f2 | cut -d " " -f1 | sed '1i\\' > forceViscous.txt
#or
#cat $1 | grep -E "viscous  : \(0" | cut -d "(" -f2 | cut -d " " -f1 | sed '1i\\' > forceViscous.txt

#Combines outputs into single file
paste time maxCourantNumber.txt meanFlowVelocity.txt forcePressure.txt forceViscous.txt>combinedResult.txt

gnuplot -p << EOF
set terminal wxt 0	#Plot 0
set style data linespoints
set key right top
set xlabel "t"
set ylabel "Maximum Courant Number"
plot "./combinedResult.txt" using 1:2 title "Max. Courant Number in x-direction"
set terminal wxt 1	#Plot 1
set style data linespoints
set key right top
set xlabel "t"
set ylabel "~u{0.7-}_x"
plot "./combinedResult.txt" using 1:3 title "Mean Flow Velocity in x-direction"
set terminal wxt 2	#Plot 2
set style data linespoints
set key right top
set xlabel "t"
set ylabel "F_x"
plot "./combinedResult.txt" using 1:4 title "Pressure Resistance in x-direction", "./combinedResult.txt" using 1:5 title "Frictional Resistance in x-direction"  
pause mouse
EOF
