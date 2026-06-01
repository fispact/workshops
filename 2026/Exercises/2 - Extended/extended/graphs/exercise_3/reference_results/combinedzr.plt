set terminal postscript landscape enhanced colour
set output "Zr_combined.ps"
#--------------------------------------------------
#       Heat Output (kW/k
set title "FNS 5 Mins Zr"
set xlabel "Time after irradiation (years)"
set ylabel "Heat Output (kW/kg)"
set logscale y
set xrange [0:60]
set yrange [*:]
#
set bmargin 6

plot \
     "Zr.gra" index   0 using ($1*365*24*60):($2*1e6)-($3*1e6):($2*1e6)+($3*1e6)  with filledcurves linecolor rgbcolor "#cbcbcb" notitle, \
     "Zr.gra" index   0 using ($1*365*24*60):($2*1e6) title  " JEFF-3.3 Heat Output" with lines linetype 1 linecolor rgbcolor "red", \
     "Zr.gra" index   1 using ($1*365*24*60):($2*1e6) title "value/t-half for nuclide (JEFF-3.3)" pointtype 1 linecolor rgbcolor "forest-green", \
     "Zr.gra" index   1 using (0.9*$1*365*24*60):($2*1e6):3 with labels notitle textcolor rgbcolor "forest-green" right font "helveticabold,11", \
     "../exercise_1/Zr.gra" index   0 using ($1*365*24*60):($2*1e6)-($3*1e6):($2*1e6)+($3*1e6)  with filledcurves linecolor rgbcolor "#cbcbcb" notitle, \
     "../exercise_1/Zr.gra" index 0 using ($1*365*24*60):($2*1e6) title  "TENDL-2017 Heat Output" with lines linetype 1 linecolor rgbcolor "green", \
     "Zr_exp.dat" using 1:2 title "experiment" with p lt 1 linecolor rgbcolor "black" pt 2 ps 0.6, \
     "Zr_exp.dat" using 1:2:3 with errorbars lt 1 linecolor rgb "black" notitle
unset label
