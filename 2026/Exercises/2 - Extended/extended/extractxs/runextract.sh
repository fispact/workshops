#!/bin/bash

GROUP=709
PNUCLIDE=H3
DNUCLIDE=H3
MT=1
PARTICLE=n

RED='\033[1;91m'
GREEN='\033[1;92m'
BLUE='\033[1;94m'
NC='\033[0m' # No Color

# A simple function to check if an error occurred while building
trycmd(){
    "$@"
    local status=$?
    if [ $status -ne 0 ]; then
        echo -e "${RED}Error occurred with $1 ${NC}" >&2
        exit $status
    fi
    return $status
}

checkvarset(){ #var
    case "${!1}" in
        yes) echo -e "Environment variable $1 is set to ${GREEN}${!1}${NC}";;
        '')  echo -e "${RED}Environment variable $1 is not set, you need to set this in order to run the script.${NC}";exit;;
        *)   echo -e "Environment variable $1 is set to ${GREEN}${!1}${NC}";;
    esac
}

checkvarset EXTRACT
checkvarset NUCLEAR_DATA

# remove any old output files
OUTPUT="extract"
if [ -f "$OUTPUT.out" ]; then
    rm "$OUTPUT.out"
fi

# write files file
FILES_FILE="files.local"
cat <<EOM > $FILES_FILE
ind_nuc ${NUCLEAR_DATA}/decay/decay_2012_index_2012
xs_endf ${NUCLEAR_DATA}/TENDL2017data/tal2017-${PARTICLE}/gxs-${GROUP}
fluxes fluxes
EOM

# write a fluxes file
FLUXES="fluxes"
for (( i=1; i<=$GROUP; i++ )); do echo 1.0; done > ${FLUXES}
echo 1.0 >> ${FLUXES}
echo "dummy flux" >> ${FLUXES}

# run extract
${EXTRACT} extract n ${GROUP} ${PNUCLIDE} ${MT} ${DNUCLIDE} ${FILES_FILE} 

# cleanup
rm ${FILES_FILE} ${FLUXES} 
