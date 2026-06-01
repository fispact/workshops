# !/bin/bash

# echo 'running TENDL17 case'

# cd TENDL2017
# $FISPACT TENDL17 files_td17

echo 'running TENDL21 case'

cd TENDL2021
$FISPACT TENDL21 files_t21

echo 'running JEFF3.3 case'

cd ../JEFF
$FISPACT JEFF files_jeff

echo 'running ENDFB8 case'

cd ../ENDFB 
$FISPACT ENDFB files_endf 

cd ../
echo 'end'
