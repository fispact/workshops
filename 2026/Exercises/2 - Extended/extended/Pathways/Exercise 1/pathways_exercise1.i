<< -----collapse cross section data----- >>
CLOBBER
SPEK
GETXS 1 709
<< -----condense decay data----- >>
GETDECAY 1
<< -----set initial conditions and get nuclear data----- >>
FISPACT
* irradiate steel
<< ----- composition ----- >>
MASS 1 1
NI 100
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