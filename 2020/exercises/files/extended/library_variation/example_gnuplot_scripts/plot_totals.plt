set terminal post eps enhanced color "Times-Roman" 20
set xlabel "Time after irradiation [minutes]"
set ylabel "Heat Output [{/Symbol m}W/g]"
set logscale y
set xr [0:60]

set xtics 0,10 out nomirror
set ytics out nomirror format "%.0E"
set border lw 1.5
set mytics 10
set mxtics 2

ylower=1e-4
yupper=1

set yr [ylower:yupper]


yclip(y) = (y<ylower)?ylower : (y>yupper)?yupper : y

show yr
show xr
set output "Nickel.eps"
set title font "Times-Roman,22" "FNS-00 5 Min. Irradiation - Ni"
plot\
     "Ni-tendl17.gra" index 4 using (($1)*365*24*60):(yclip(($2)*1E+06+($3)*1E+06)):(yclip(($2)*1E+06-($3)*1E+06)) every ::1 notitle with filledcurves lt 10 lw 0.2 lc rgbcolor "#CFCFCF",\
     "5m_Exp_mod.data"  using 1:2 title "FNS Experiment" with p lt 1 linecolor rgb "black" pt 2 ps 0.6, \
     "" using 1:2:3 with errorbars lt 1 linecolor rgb "black" notitle,\
     "Ni-jeff33.gra" index 4 using (($1)*365*24*60):(($2)*1E+06) every ::1 title "JEFF-3.3" with lines lt 1 dt (12,4,2,4) lw 2.0 lc rgbcolor "green", \
     "Ni-b8.gra" index 4 using (($1)*365*24*60):(($2)*1E+06) every ::1 title "ENDF/B-VIII.0" with lines lt 1 dt (8,4,2,4,2,4) lw 2.0 lc rgbcolor "black", \
     "Ni-tendl17.gra" index 4 using (($1)*365*24*60):(($2)*1E+06) every ::1 title "TENDL-2017" with lines lt 1 lw 2.0 lc rgbcolor "red",\

unset output

