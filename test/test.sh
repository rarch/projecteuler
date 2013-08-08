#!/bin/bash
# will test all project euler problems and makefiles
PROJECT=$PWD/".."
TEST=$PROJECT/"test"
PROBS=434

EXTENSIONS=( "py" "rb" )

HSSUFF="_hs.out"
MAKEFILE="Makefile"

control_c() {
    exit -1
}

trap control_c SIGINT
# go through all project euler problems 1..434, convert number to string
for i in $(seq 1 $PROBS)
do
#   fail if any subsequent steps fail
    subdir=$($TEST/numword.py $i)
#   check if projecteuler directory contains subdir with that name, and cd to it
    if [ -d $PROJECT/$subdir ]; then
        echo $subdir":"
#       in subdir check for executable files that start with same name with extension py, rb, and run them
        for file in $PROJECT/$subdir/$subdir*
        do
            filebasename=$(basename "$file")
            ext="${filebasename##*.}"
            # filename="${filebasename%.*}"

            if [ -x $file ]; then
                for acceptable in ${EXTENSIONS[@]}
                do
                    if [ "$ext" = "$acceptable" ]; then
                    # && [ "$filename" = "$subdir" ]; then

                    # check for hs file, check for makefile
                    # check make rm haskell, make haskell, clean haskell, proper output
                    # make rm haskell
                    
                        output=$($file)
                        echo -ne " "$filebasename
                        echo -ne "="$output
                    fi
                done
            fi
        done
        echo
#       check for makefile

#           make, check output
#           make clean, check output
#           check for executable files that end in _hs.out, and run it, print labeled output
#           make rm, check output
        echo
    fi
done
#   exit