#!/bin/sh

gnuplot -p << EOF
set terminal wxt 0
set style data linespoints
set key right bottom
set xlabel "y^+"
set ylabel "~u{0.7-}^+"
plot "./postProcessing/sample/588/wallNormal_U.xy" using 1:2 title "RANS"
set terminal wxt 1
set style data linespoints
set key right top
set xlabel "y^+"
set ylabel "k^+, {u'v'}^+"
plot "./postProcessing/sample/588/wallNormal_k.xy" using 1:2 title "k^+ RANS", "./postProcessing/sample/588/wallNormal_R.xy" using 1:3 title "{u'v'}^+ RANS"
pause mouse
EOF
