CLOBBER
MONITOR 1
<< -----get nuclear data----- >>
GETXS 1 709
GETDECAY 1
FISPACT
* W
<< -----set initial conditions----- >>
MASS 1.0 1
W 100.0
<< No graphs, cutof for dom nuc, inc. uncert., graph types >>
NUCGRAPH 3 1.0 0 1 2 3
ATOMS
HALF 
<< -----irradiation phase----- >>
TIME 2.5 YEARS 
ATOMS
<< -----cooling phase----- >>
FLUX 0.
ZERO

PULSE 1000
 TIME 24.0 HOURS ATOMS
ENDPULSE
END
* END
