<< -----collapse cross section data----- >>
CLOBBER
JSON
SPEK
GETXS 1 709
<< -----condense decay data----- >>
GETDECAY 1
<< -----set initial conditions and get nuclear data----- >>
FISPACT
* irradiate steel
<< ----- steel composition ----- >>
DENSITY 7.9
MASS 1 13
FE 61.395 
C 0.03 
MN  2.0 
CR 18.5 
NI  12 
P 0.035 
S  0.03 
SI  1.0 
MO  2.3 	
O  1.2 
N  1.0 
NB  0.01
SN 0.5 
<< -----other initialisation options----- >>
MIND 1.0E5
HAZARDS
HALF
UNCERTAINTY 2
<< -----irradiation phase----- >>
ATOMS
FLUX 7.47205E+13
TIME 1 YEARS
ATOMS
<< -----cooling phase----- >>
FLUX 0.0
ZERO
END
* END