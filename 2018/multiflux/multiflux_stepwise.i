<< -----get nuclear data----- >>
CLOBBER
XSTHRESH 1.0e-15
MONITOR 1
GETXS 0
GETDECAY 0
FISPACT
* IRRADIATION OF Ar

<< -----set initial conditions----- >>
FUEL 1
Ar40 1e25
DENSITY 0.1
ATOMS

<< -----1.1 plasma irradiation phase----- >>
FLUX 2.12437E14
TIME 2 SECS ATOMS

<< -----1.2 divertor irradiation phase----- >>
GETXS 0
FLUX 5.9558E+14
TIME 10 SECS ATOMS


FLUX 0.0
ZERO
TIME 1 YEAR
ATOMS

END
* END
