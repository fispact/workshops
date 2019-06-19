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
MASS 1 4
FE 80
C 2
CR 10
NI 8
<< -----other initialisation options----- >>
MIND 1.0E5
HAZARDS
HALF
UNCERTAINTY 2
<< -----irradiation phase----- >>
ATOMS
FLUX 7.47205E+13
TIME 60 
ATOMS
<< -----cooling phase----- >>
FLUX 0.0
ZERO
END
* END