set terminal postscript landscape enhanced colour
set output "combine.gra.ps"
#--------------------------------------------------
#          Activity (Bq/k
set title "Cobalt"
set xlabel "Time after irradiation (years)"
set ylabel "Activity (Bq/kg)"
set logscale xy
set xrange [ 1.00000E-04: 1.00000E-01]
set yrange [*:]
#
set bmargin 6
set label "file name = combine.gra          run timestamp = 10:42:35 18 June 2024" \
 at character 1,1 font "Helvetica,8pt"
plot \
     "combine.gra" index   0 using 1:($2)-($3):($2)+($3)  with filledcurves linecolor rgbcolor "#cbcbcb" notitle, \
     "combine.gra" index   0 using 1:2 title  "         Activity (Bq/kg)" with lines linetype 1 linecolor rgbcolor "red", \
     "combine.gra" index   0 using 1:2:3 with yerrorbars title "Uncertainty" linetype 1 linecolor rgb "black", \
     "combine.gra" index   1 using 1:2 title "value/t-half for nuclide" pointtype 1 linecolor rgbcolor "forest-green", \
     "combine.gra" index   1 using (0.8*$1):2:3 with labels notitle textcolor rgbcolor "forest-green" right font "helveticabold,11"
unset label
# pause -1  "Hit return to continue"
#--------------------------------------------------
#       Heat Output (kW/k
set title "Cobalt"
set xlabel "Time after irradiation (years)"
set ylabel "Heat Output (kW/kg)"
set logscale xy
set xrange [ 1.00000E-04: 1.00000E-01]
set yrange [*:]
#
set bmargin 6
set label "file name = combine.gra          run timestamp = 10:42:35 18 June 2024" \
 at character 1,1 font "Helvetica,8pt"
plot \
     "combine.gra" index   2 using 1:($2)-($3):($2)+($3)  with filledcurves linecolor rgbcolor "#cbcbcb" notitle, \
     "combine.gra" index   2 using 1:2 title  "      Heat Output (kW/kg)" with lines linetype 1 linecolor rgbcolor "red", \
     "combine.gra" index   2 using 1:2:3 with yerrorbars title "Uncertainty" linetype 1 linecolor rgb "black", \
     "combine.gra" index   3 using 1:2 title "value/t-half for nuclide" pointtype 1 linecolor rgbcolor "forest-green", \
     "combine.gra" index   3 using (0.8*$1):2:3 with labels notitle textcolor rgbcolor "forest-green" right font "helveticabold,11"
unset label
# pause -1  "Hit return to continue"
