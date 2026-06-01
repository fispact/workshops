CLOBBER
NOFISS
<< -----collapse cross section data----- >>
GETXS 1 709
<< -----condense decay data----- >>
GETDECAY 1
<< -----self-shielding correction----- >>
PROBTABLE 0 1
SSFCHOOSE 1 0
W
SSFMASS 1.0 1
W 100.0 
FISPACT
* transmutation run 
 MASS 1.0  1
 W 100.0 
<< -----irradiation phase----- >> 
FLUX 3.0+14
TIME 10 YEARS
ATOMS
END
* END OF RUN
