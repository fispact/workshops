set terminal post eps enhanced color "Times-Roman" 20
set table "one13.dat"
splot "/work/validation/fns/fispact_runs/new3t5-17/Ni.gra" index 4 using (($1)*365*24*60):(($2)*1E+06):(($3)*1E+06) every ::1 notitle
unset table
set table "onecase4.dat"
splot "/work/validation/fns/fispact_runs/new3t5-b8/Ni.gra" index 4 using (($1)*365*24*60):(($2)*1E+06):(($3)*1E+06) every ::1  notitle
unset table
set table "onecase2.dat"
splot "/work/validation/fns/fispact_runs/new3t5-j33/Ni.gra" index 4 using (($1)*365*24*60):(($2)*1E+06):(($3)*1E+06) every ::1  notitle
unset table
set table "onecase3.dat"
splot "/work/validation/fns/fispact_runs/new3t5-10/Ni.gra" index 4 using (($1)*365*24*60):(($2)*1E+06):(($3)*1E+06) every ::1  notitle
unset table
set table "oneexp.dat"
splot "<awk 'NR==398,NR==418{print $1,$2,$3}' ../fns_exp_results//5m_Exp_mod.data"  using ($1>0?$1:1/0):2:3 notitle
unset table 
set table "onesubsetcase1.dat"
splot "/work/validation/fns/fispact_runs/new3t5-irdff/Ni.gra" index 4 using (($1)*365*24*60):(($2)*1E+06):(($3)*1E+06) every ::1  notitle
unset table 
set xlabel "Time after irradiation [minutes]"
set ylabel "Heat Output [{/Symbol m}W/g]"
set logscale y
set xr [0:60]
set yr [*:*] writeback
set xtics 0,10 out nomirror
set ytics out nomirror format "%.0E"
set border lw 1.5
set mytics 10
set mxtics 2
# skipping first data point in every decay graph - see "every ::1"
set output "test.ps"

plot\
     "<awk 'NR==398,NR==418{print $1,$2,$3}' ../fns_exp_results//5m_Exp_mod.data"  using 1:($2*0.5) title "FNS Experiment" with p, \
     "" using 1:2:3 with errorbars notitle,\
     "/work/validation/fns/fispact_runs/new3t5-j33/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06*0.5) every ::1 title "JEFF-3.3" with lines, \
     "/work/validation/fns/fispact_runs/new3t5-10/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06*0.5) every ::1 title "EAF2010" with lines, \
     "/work/validation/fns/fispact_runs/new3t5-b8/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06*0.5) every ::1 title "ENDF/B-VIII.0" with lines, \
     "/work/validation/fns/fispact_runs/new3t5-17/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06*0.5) every ::1 title "TENDL-2017" with lines,\
"/work/validation/fns/fispact_runs/new3t5-irdff/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06*0.5) every ::1 title "IRDFF-1.05" with lines,\

ylower=GPVAL_Y_MIN
set yr [ylower:*] writeback
show yr 

plot\
     "<awk 'NR==398,NR==418{print $1,$2,$3}' ../fns_exp_results//5m_Exp_mod.data"  using 1:($2*2) title "FNS Experiment" with p, \
     "" using 1:2:3 with errorbars notitle,\
     "/work/validation/fns/fispact_runs/new3t5-j33/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06*2) every ::1 title "JEFF-3.3" with lines, \
     "/work/validation/fns/fispact_runs/new3t5-10/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06*2) every ::1 title "EAF2010" with lines, \
     "/work/validation/fns/fispact_runs/new3t5-b8/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06*2) every ::1 title "ENDF/B-VIII.0" with lines, \
     "/work/validation/fns/fispact_runs/new3t5-17/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06*2) every ::1 title "TENDL-2017" with lines,\
"/work/validation/fns/fispact_runs/new3t5-irdff/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06) every ::1 title "IRDFF-1.05" with lines lc rgbcolor "cyan",\

set yr restore
show yr
#save "|grep yr >out2.temp"
#ylower=system("awk '{ if($2 ~ /yrange/) {print $4} }' out2.temp")
#yupper=system("awk '{ if($2 ~ /yrange/) {print $6} }' out2.temp")

yupper=GPVAL_Y_MAX

set lmargin 10
if (ylower<1) {ticvalue=10**(int(log10(ylower))-1)} else {ticvalue=10**(int(log10(ylower)))}
print ylower,yupper,ticvalue

if ((log10(yupper)-log10(ylower))<0.3) {ticvalue=ticvalue;set ytics format "%.1E";set yl offset 0.9,0;set mytics 2}
else {if ((log10(yupper)-log10(ylower))<(log10(2.0)-log10(0.5))) {ticvalue=ticvalue*2;set ytics format "%.1E";set yl offset 0.9,0;set mytics 2}
else {if ((log10(yupper)-log10(ylower))<1.1) {ticvalue=ticvalue*10;set ytics format "%.1E";set yl offset 0.9,0;set mytics 2}
else {if ((log10(yupper)-log10(ylower))<1.5) {ticvalue=ticvalue*20;set ytics format "%.1E";set yl offset 0.9,0;set mytics 2}}}}

if ((log10(yupper)-log10(ylower))<1.5) {
yvalue=ticvalue
while (yvalue<ylower) {yvalue=yvalue+ticvalue}
#define min value tic
#starting from 0.5, first above ylower
minytic=yvalue*0.5
while (minytic <ylower) {minytic=minytic+yvalue*0.1}
set ytics (minytic)
while (yvalue<yupper) {set ytics add (yvalue, yvalue+ticvalue/2 1)
yvalue=yvalue+ticvalue}
}

#if ((log10(yupper)-log10(ylower))<(log10(2.0)-log10(0.5))) {set ytics ticvalue*2 format "%.1E";set yl offset 0.9,0;set mytics 2}
#else {if ((log10(yupper)-log10(ylower))<1.0) {set ytics ticvalue*5 format "%.1E";set ylabel offset 0.9,0;set mytics 1}
#else {if ((log10(yupper)-log10(ylower))<1.5) {set ytics ticvalue*20 format "%.1E";set ylabel offset 0.9,0;set mytics 2}}}
show ytics
yclip(y) = (y<ylower)?ylower : (y>yupper)?yupper : y

show yr
show xr
set output "plots/Nickel_one.eps"
set title font "Times-Roman,22" "FNS-00 5 Min. Irradiation - Ni"
plot\
     "/work/validation/fns/fispact_runs/new3t5-17/Ni_highres.gra" index 4 using (($1)*365*24*60):(yclip(($2)*1E+06+($3)*1E+06)):(yclip(($2)*1E+06-($3)*1E+06)) every ::1 notitle with filledcurves lt 10 lw 0.2 lc rgbcolor "#CFCFCF",\
     "<awk 'NR==398,NR==418{print $1,$2,$3}' ../fns_exp_results//5m_Exp_mod.data"  using 1:2 title "FNS Experiment" with p lt 1 linecolor rgb "black" pt 2 ps 0.6, \
     "" using 1:2:3 with errorbars lt 1 linecolor rgb "black" notitle,\
     "/work/validation/fns/fispact_runs/new3t5-j33/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06) every ::1 title "JEFF-3.3" with lines lt 1 dt (12,4,2,4) lw 2.0 lc rgbcolor "green", \
     "/work/validation/fns/fispact_runs/new3t5-10/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06) every ::1 title "EAF2010" with lines lt 1 dt (5,5) lw 2.0 lc rgbcolor "blue", \
     "/work/validation/fns/fispact_runs/new3t5-b8/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06) every ::1 title "ENDF/B-VIII.0" with lines lt 1 dt (8,4,2,4,2,4) lw 2.0 lc rgbcolor "black", \
     "/work/validation/fns/fispact_runs/new3t5-17/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06) every ::1 title "TENDL-2017" with lines lt 1 lw 2.0 lc rgbcolor "red",\
"/work/validation/fns/fispact_runs/new3t5-irdff/Ni_highres.gra" index 4 using (($1)*365*24*60):(($2)*1E+06) every ::1 title "IRDFF-1.05" with lines lt 1 dt (6,4,6,4,2,4) lw 2.0 lc rgbcolor "cyan",\

unset output

