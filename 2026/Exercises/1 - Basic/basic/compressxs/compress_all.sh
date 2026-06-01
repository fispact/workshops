#!/bin/bash

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

checkvarset COMPRESS
checkvarset NUCLEAR_DATA
checkvarset NUCLEAR_DATA_BIN

trycmd mkdir -p ${NUCLEAR_DATA_BIN}
trycmd cd ${NUCLEAR_DATA_BIN}

OPTION=5

compressTENDL(){ #year, #particle, #group
    local year="$1"
    local particle="$2"
    local group="$3"

    echo -e "${BLUE}TENDL20"${year}"-"${particle}" ${NC}..."
    filesfile=files.tendl20${year}${particle}
cat > $filesfile <<EOF
ind_nuc ${NUCLEAR_DATA}/TENDL20${year}data/tendl${year}_decay12_index
xs_endf ${NUCLEAR_DATA}/TENDL20${year}data/tal20${year}-${particle}/gxs-${group}
EOF
    trycmd time $COMPRESS tal20${year}-${particle} ${particle} ${group} $OPTION $filesfile
}

compressTENDL 14 n 709
compressTENDL 14 p 162
compressTENDL 14 a 162
compressTENDL 14 g 162
compressTENDL 14 d 162

compressTENDL 15 n 709
compressTENDL 15 p 162
compressTENDL 15 a 162
compressTENDL 15 g 162
compressTENDL 15 d 162

compressTENDL 17 n 709
compressTENDL 17 p 162
compressTENDL 17 a 162
compressTENDL 17 g 162
compressTENDL 17 d 162
compressTENDL 17 h 162
compressTENDL 17 t 162
