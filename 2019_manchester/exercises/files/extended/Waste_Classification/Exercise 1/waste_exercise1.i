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
MASS 1 9
FE 62.395
C 0.03
MN 2.0 
CR 18.5
NI 13.5
P 0.045
S 0.03
SI 1.0
MO 2.5
<< -----other initialisation options----- >>
MIND 1.0E5
HAZARDS
HALF
<< -----irradiation phase----- >>
ATOMS
FLUX 2.29068E14
TIME 24 HOURS
ATOMS
<< -----cooling phase----- >>
FLUX 0.0
ZERO
TIME 1 YEARS
ATOMS
TIME 4 YEARS
ATOMS
TIME 5 YEARS
ATOMS
TIME 10 YEARS
ATOMS
TIME 10 YEARS
ATOMS
TIME 10 YEARS
ATOMS
TIME 10 YEARS
ATOMS
TIME 25 YEARS
ATOMS
TIME 25 YEARS
ATOMS
TIME 50 YEARS
ATOMS
TIME 50 YEARS
ATOMS
TIME 50 YEARS
ATOMS
TIME 50 YEARS
ATOMS
TIME 100 YEARS
ATOMS
TIME 100 YEARS
ATOMS
END
* END