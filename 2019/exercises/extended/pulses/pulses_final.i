<< -- CONTROL -->>
GETXS 1 709
GETDECAY 1
FISPACT
* Exact ITER Irradiation Scenario
DENSITY 7.8
MASS 1.0 9
FE 65.050
C   0.030
MN  2.000
P   0.045
S   0.030
SI  0.750
CR  20.00
NI  12.00
N    0.10
MIND 1.
UNCERTAINTY 3
HALF
HAZARDS
<< -- IRRADIATION -- >>
FLUX 1.0E13
PULSE 52 << 52 weeks >> 
  FLUX 0.0
  TIME 2 DAYS << dont work on weekends >>
  ATOMS
  PULSE 5 << 5 days of work >>
    FLUX 0.0
    TIME 16.0 HOURS ATOMS
    PULSE 16 << 16 pulses per day >> 
      FLUX 0.0
      TIME 30.0 MINS ATOMS << 30 mins off >>
      FLUX 1.0E13 
      TIME 5 ATOMS << 5 seconds on >>
     ENDPULSE 
  ENDPULSE
ENDPULSE
FLUX 0.0
ZERO
<< -- DECAY -- >>
TIME 0 ATOMS << shutdown >> 
TIME 5 MINS ATOMS 
TIME 55 MINS ATOMS
TIME 23 HOURS ATOMS
TIME 29 DAYS ATOMS << 30 DAYS >>
TIME 30 DAYS ATOMS << 60 DAYS >>
TIME 30 DAYS ATOMS << 90 DAYS >>
TIME 90 DAYS ATOMS << 180 DAYS >>
TIME 185.25 DAYS ATOMS << 1 Year>>
TIME 1 YEARS ATOMS << 2 Years >>
TIME 1 YEARS ATOMS << 3 Years >> 
TIME 2 YEARS ATOMS << 5 Years >>
TIME 5 YEARS ATOMS << 10 Years >> 
TIME 10 YEARS ATOMS << 20 Years >>
TIME 10 YEARS ATOMS << 30 Years >>
TIME 20 YEARS ATOMS << 50 Years >>
TIME 50 YEARS ATOMS << 100 Years >>
END 
* end of irradiation
