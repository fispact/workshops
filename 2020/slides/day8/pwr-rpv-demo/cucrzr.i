<< -----get nuclear data----- >>

CLOBBER
GETXS 0
GETDECAY 0
FISPACT
* Tungsten Carbide
<< -----set initial conditions----- >>
DENSITY 8.89
MASS 1.0 3
Cu 99.29
Cr 0.61
Zr 0.1
MIND 1.E5
HAZA
CLEAR
HALF
FLUX 1.1234E+11
ATOMS
<< -----irradiation phase----- >>
TIME 1.0 YEARS
ATOMS
<< -----cooling phase----- >>
FLUX 0.
ZERO
TIME 1 DAYS ATOMS
TIME 9 DAYS ATOMS
TIME 90 DAYS ATOMS
TIME 265.25 DAYS ATOMS
TIME 9 YEARS ATOMS
TIME 90 YEARS ATOMS
TIME 900 YEARS ATOMS
END
* END

