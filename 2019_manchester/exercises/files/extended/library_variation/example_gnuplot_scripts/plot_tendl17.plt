
set term postscript color enhanced font ",25"
 
reset
set colors classic
##lw 3
#set lt 1 dt 1 lw 0.8
#set lt 2 dt (10,5)
#set lt 3 dt (5,6)
#set lt 4 dt (3,4)
#set lt 5 dt (14,4,2,4)
#set lt 6 dt (6,5,2,5)
#set lt 7 dt (5,5,5,15)
#set lt 8 dt (2,4,12,4,2,4)
#set lt 9 dt (5,5,5,5,5,5,5,10)
#set lt 10 dt 1 lw 0.8
#set lt 11 dt (10,5)
#set lt 12 dt (5,6)
#set lt 13 dt (3,4)
#set lt 14 dt (14,4,2,4)
#set lt 15 dt (6,5,2,5)
#set lt 16 dt (5,5,5,15)
#set lt 17 dt (2,4,12,4,2,4)
#set lt 18 dt (5,5,5,5,5,5,5,10)


#lw 5 
set lt 1 dt 1 lw 0.8
set lt 2 dt (2.5,1.25)
set lt 3 dt (1.25,1.5)
set lt 4 dt (0.75,1.0)
set lt 5 dt (3.5,1,0.5,1)
set lt 6 dt (1.5,1.25,0.5,1.25)
set lt 7 dt (1.25,1.25,1.25,3.75)
set lt 8 dt (0.5,1,3,1,0.5,1)
set lt 9 dt (1.25,1.25,1.25,1.25,1.25,1.25,1.25,2.5) 
set lt 10 dt 1 lw 0.8
set lt 11 dt (2.5,1.25)
set lt 12 dt (1.25,1.5)
set lt 13 dt (0.75,1.0)
set lt 14 dt (3.5,1,0.5,1)
set lt 15 dt (1.5,1.25,0.5,1.25)
set lt 16 dt (1.25,1.25,1.25,3.75)
set lt 17 dt (0.5,1,3,1,0.5,1)
set lt 18 dt (1.25,1.25,1.25,1.25,1.25,1.25,1.25,2.5)


set logscale y
set logscale x

set xr [2e-6:1.140771E-04]
set label 101 at 1.1408e-4,graph(1.05) "Hour" tc rgbcolor "blue" center
set arrow 101 from 1.1408e-4,graph(0.0) to 1.1408e-4,graph(1.01) lt 3 lw 1.4 lc rgbcolor "black" nohead

set label 102 at 9.5064e-6,graph(1.05) "5m" tc rgbcolor "blue" center
set label 103 at 1.9013e-5,graph(1.05) "10m" tc rgbcolor "blue" center
set arrow 102 from 9.5064e-6,graph(0.0) to 9.5064e-6,graph(1.01) lt 3 lw 1.4 lc rgbcolor "black" nohead
set arrow 103 from 1.9013e-5,graph(0.0) to 1.9013e-5,graph(1.01) lt 3 lw 1.4 lc rgbcolor "black" nohead

set yr [1.000000E-04/10:1.000000E+00]
set xtics out nomirror format "%.0E"
set ytics out nomirror format "%.0E"
set border lw 1.5
set mytics 10
set mxtics 10
set clip one
set clip two
set title font "Times-Roman,22" "FNS-00 5 Min. Irradiation - Ni - TENDL-2017"  offset 0,0.5
set xlabel "Time after irradiation [years]"

colours(n)=word("web-green magenta red navy web-blue dark-grey dark-goldenrod cyan light-green purple steelblue orange dark-red midnight-blue light-goldenrod aquamarine plum light-blue midnight-blue yellow dark-violet dark-olivegreen bisque greenyellow salmon light-red sea-green sandybrown grey cyan web-green magenta black red navy web-blue dark-grey dark-goldenrod cyan light-green purple steelblue dark-cyan orange dark-red light-goldenrod aquamarine plum light-blue midnight-blue yellow dark-violet dark-olivegreen bisque greenyellow salmon light-red sea-green sandybrown grey cyan purple ",n)
# need ytics to be small to get best range in plot - no idea why this works.
 
#set label 50 at graph 1.0,graph 1.08 "\nHeat Output" right font ",18"

set key at graph 1.05,graph 1.0 left reverse Left samplen 1.4 horizontal maxcols 1 width -1 font ",23"

set output 'Nickel_17_nuclide.ps'

#set yl "Heat Output [{/Symbol m}W/g]"
set yl "" 
set label 150 at graph -0.20,graph 0.5 center rotate by 90 "Heat Output [{/Symbol m}W/g]"
pl \
"Ni-tendl17.grn" \
 u (($2)):($4*1e6) \
every ::2+1 not w l lt 1 lw 6 lc rgbcolor "black",\
"Ni-tendl17.grn" \
 u (($2)):($4*1e6) \
every 10::9+2 t "total" w p lt 1 lw 6 lc rgbcolor "black",\
"Ni-tendl17.grn" \
 u (($2)):($10>1e-13/10?$10*1e6:1/0) \
every ::2+1 not w l lt 2 lw 5 lc rgbcolor colours(1),\
"Ni-tendl17.grn" \
 u (($2)):($10>1e-13/10?$10*1e6:1/0) \
every 10::9+2 t "Co58" w p lt 2  lw 5 lc rgbcolor colours(1),\
"Ni-tendl17.grn" \
 u (($2)):($11>1e-13/10?$11*1e6:1/0) \
every ::2+1 not w l lt 3 lw 5 lc rgbcolor colours(2),\
"Ni-tendl17.grn" \
 u (($2)):($11>1e-13/10?$11*1e6:1/0) \
every 10::9+2 t "Co58m" w p lt 3  lw 5 lc rgbcolor colours(2),\
"Ni-tendl17.grn" \
 u (($2)):($12>1e-13/10?$12*1e6:1/0) \
every ::2+1 not w l lt 4 lw 5 lc rgbcolor colours(3),\
"Ni-tendl17.grn" \
 u (($2)):($12>1e-13/10?$12*1e6:1/0) \
every 10::9+2 t "Co61" w p lt 4  lw 5 lc rgbcolor colours(3),\
"Ni-tendl17.grn" \
 u (($2)):($13>1e-13/10?$13*1e6:1/0) \
every ::2+1 not w l lt 5 lw 5 lc rgbcolor colours(4),\
"Ni-tendl17.grn" \
 u (($2)):($13>1e-13/10?$13*1e6:1/0) \
every 10::9+2 t "Fe61" w p lt 5  lw 5 lc rgbcolor colours(4),\
"Ni-tendl17.grn" \
 u (($2)):($14>1e-13/10?$14*1e6:1/0) \
every ::2+1 not w l lt 6 lw 5 lc rgbcolor colours(5),\
"Ni-tendl17.grn" \
 u (($2)):($14>1e-13/10?$14*1e6:1/0) \
every 10::9+2 t "Ni57" w p lt 6  lw 5 lc rgbcolor colours(5),\
"Ni-tendl17.grn" \
 u (($2)):($15>1e-13/10?$15*1e6:1/0) \
every ::2+1 not w l lt 7 lw 5 lc rgbcolor colours(6),\
"Ni-tendl17.grn" \
 u (($2)):($15>1e-13/10?$15*1e6:1/0) \
every 10::9+2 t "Co60m" w p lt 7  lw 5 lc rgbcolor colours(6),\
"Ni-tendl17.grn" \
 u (($2)):($16>1e-13/10?$16*1e6:1/0) \
every ::2+1 not w l lt 8 lw 5 lc rgbcolor colours(7),\
"Ni-tendl17.grn" \
 u (($2)):($16>1e-13/10?$16*1e6:1/0) \
every 10::9+2 t "Co62m" w p lt 8  lw 5 lc rgbcolor colours(7),\
"Ni-tendl17.grn" \
 u (($2)):($17>1e-13/10?$17*1e6:1/0) \
every ::2+1 not w l lt 9 lw 5 lc rgbcolor colours(8),\
"Ni-tendl17.grn" \
 u (($2)):($17>1e-13/10?$17*1e6:1/0) \
every 10::9+2 t "Co62" w p lt 9  lw 5 lc rgbcolor colours(8),\
"5m_Exp_mod.data"  using ($1/60/24/365.25):2 title "00 Exp" with p lt 1 linecolor rgb "grey" pt 9 ps 1.5, \
     "" using ($1/60/24/365.25):2:3 with errorbars lt 1 linecolor rgb "grey" notitle,\
     
     
unset output
