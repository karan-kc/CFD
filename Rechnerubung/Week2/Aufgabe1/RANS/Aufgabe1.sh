#!/bin/sh

gnuplot -p << EOF
set terminal wxt 0	#Plot 0
set style data linespoints
set key right bottom
set xlabel "y^+"
set ylabel "~u{0.7-}^+"
plot "./postProcessing/sample/588/wallNormal_U.xy" using 1:2 title "RANS", "./Re180.prof" using 2:3 title "DNS"
set terminal wxt 1	#Plot 1
set style data linespoints
set key right top
set xlabel "y^+"
set ylabel "k^+, {u'v'}^+"
plot "./postProcessing/sample/588/wallNormal_k.xy" using 1:2 title "k^+ RANS", "./postProcessing/sample/588/wallNormal_R.xy" using 1:3 title "{u'v'}^+ RANS", "./Re180.prof" using 2:((\$4**2+\$5**2+\$6**2)/3) title "k^+ DNS", "./Re180.prof" using 2:11 title "{u'v'}^+ DNS"
pause mouse
EOF
