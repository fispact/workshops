set terminal postscript landscape enhanced colour
set output "inventory.gra.ps"
#--------------------------------------------------
#       Heat Output (kW/k
set title "FNS 5 Minutes Inconel-600"
set xlabel "Time after irradiation (years)"
set ylabel "Heat Output (kW/kg)"
set logscale xy
set xrange [ 1.00000E-06: 1.00000E-03]
set yrange [*:]
#
set bmargin 6
set label "file name = inventory.gra          run timestamp = 14:24:00 8 June 2018" \
 at character 1,1 font "Helvetica,8pt"
plot \
     "inventory.gra" index   0 using 1:($2)-($3):($2)+($3)  with filledcurves linecolor rgbcolor "#cbcbcb" notitle, \
     "inventory.gra" index   0 using 1:2 title  "      Heat Output (kW/kg)" with lines linetype 1 linecolor rgbcolor "red", \
     "inventory.gra" index   0 using 1:2:3 with yerrorbars title "Uncertainty" linetype 1 linecolor rgb "black", \
     "inventory.gra" index   1 using 1:2 title "value/t-half for nuclide" pointtype 1 linecolor rgbcolor "forest-green", \
     "inventory.gra" index   1 using (0.8*$1):2:3 with labels notitle textcolor rgbcolor "forest-green" right font "helveticabold,11"
unset label
# pause -1  "Hit return to continue"
