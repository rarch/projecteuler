#!/bin/bash
# will run my project euler problem solutions

TESTHOME=$PWD
PROJECT=$TESTHOME/".."
PROBS=434
EXTENSIONS=( "py" "rb" )
DOTHS=".hs"
HSSUFF="_hs.out"
MAKEFILE="Makefile"
README="README.md"
PREFIX=">>>\t"

directories=()

[ -f $PROJECT/$README ] || { echo ; echo no readme ; exit 1 ; }

echo -e "${PREFIX}GETTING LIST OF DIRECTORIES"
# go through all project euler problems 1..434, convert number to string
for i in $(seq 1 $PROBS)
do
    subdir=$($TESTHOME/numword.rb $i)
    # subdir=$($TESTHOME/numword.py $i)
    # subdir=$($TESTHOME/numword.sh $i) # in progress
    if [ -d $PROJECT/$subdir ]; then
        directories+=("$subdir")
    fi
done
echo -e "${PREFIX}GOT"

echo -e "${PREFIX}TESTING FILES"
for subdir in ${directories[@]}
do
    echo ; echo $subdir":"

    for file in $PROJECT/$subdir/$subdir*
    do
        filebasename=$(basename "$file")
        ext="${filebasename##*.}"
        # filename="${filebasename%.*}"

        if [ -x $file ]; then
            for acceptable in ${EXTENSIONS[@]}
            do
                if [ "$ext" = "$acceptable" ]; then # && [ "$filename" = "$subdir" ]; then
                    output=$($file) || { echo ; echo $filebasename ; exit 2 ; } #should check output against value, get this from README
                    echo -ne $filebasename"="$output" ; "
                fi
            done
        fi
    done

    # test haskell files if there is a makefile
    if [ -f $PROJECT/$subdir/$MAKEFILE ]; then
        cd $PROJECT/$subdir

        filebasename=$(basename "$PROJECT/$subdir/$subdir$DOTHS")
        if [ -f $PROJECT/$subdir/$subdir$DOTHS ]; then

            # echo ; echo -e "${PREFIX}MAKING $HSSUFF FROM $DOTHS"
            make rm -s || { echo ; echo make rm ; exit 3 ; }
            make -s > /dev/null 2>&1 || { echo ; echo make ; exit 4 ; } # do not print messy output from makefile
            make clean -s || { echo ; echo make clean ; exit 5 ; }

            echo -n "make works ; "
            output=$($PROJECT/$subdir/$subdir$HSSUFF) || { echo ; echo $filebasename ; exit 2 ; } #should check output against value, get this from README
            echo -ne $filebasename"="$output" ; "

            make rm -s || { echo ; echo make rm ; exit 3 ; }
        fi
        cd $TESTHOME
    fi
    echo
done

echo ; echo -e "${PREFIX}COMPLETE"
exit 0