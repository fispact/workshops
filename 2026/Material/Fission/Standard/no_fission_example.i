<< -----set initial conditions and get nuclear data----- >>
CLOBBER
MONITOR 1
GETXS 1 709
GETDECAY 1
NOFISS
FISPACT
* no fission example
<< ----- define UO2 taken from PNNL Compendium  ----- >>
FUEL 7
    U234 1E20
    U235 1.0124E23
    U236 4.6E20
    U238 3.230772E24
    O16 6.65047E24
    O17 2.53E21
    O18 1.367E25
DENSITY 10.96
<< -----other initialisation options----- >>
MIND 1.0E5
HAZARD
HALF
<< -----irradiation phase----- >>
ATOMS
FLUX 1E13
TIME 91.3 DAY ATOMS
TIME 91.3 DAY ATOMS
TIME 91.3 DAY ATOMS
TIME 91.3 DAY ATOMS
<< -----cooling phase----- >>
FLUX 0.
ZERO
TIME 1 HOUR ATOMS
TIME 23 HOUR ATOMS
TIME 364 DAY ATOMS
TIME 4 YEAR ATOMS
TIME 5 YEAR ATOMS
TIME 40 YEAR ATOMS
TIME 50 YEAR ATOMS
END
* END
