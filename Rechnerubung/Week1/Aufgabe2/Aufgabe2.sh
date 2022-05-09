#!/bin/sh

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
