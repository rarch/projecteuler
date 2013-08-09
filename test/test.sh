#!/bin/bash
# will test all project euler problems and makefiles

TESTHOME=$PWD
PROJECT=$TESTHOME/".."
PROBS=434
EXTENSIONS=( "py" "rb" )
DOTHS=".hs"
HSSUFF="_hs.out"
MAKEFILE="Makefile"
PRE=">>>\t"

directories=()

echo -e "${PRE}GETTING LIST OF DIRECTORIES"
# go through all project euler problems 1..434, convert number to string
for i in $(seq 1 $PROBS)
do
    subdir=$($TESTHOME/numword.py $i)
    if [ -d $PROJECT/$subdir ]; then
        directories+=("$subdir")
    fi
done
echo -e "${PRE}GOT"

echo -e "${PRE}TESTING FILES"
for subdir in ${directories[@]}
do
    echo
    echo $subdir":"

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
                    output=$($file) #should check output against value, get this from README
                    echo -ne " "$filebasename
                    echo -ne "="$output
                fi
            done
        fi
    done

    # test haskell files if there is a makefile
    if [ -f $PROJECT/$subdir/$MAKEFILE ]; then
        cd $PROJECT/$subdir

        filebasename=$(basename "$PROJECT/$subdir/$subdir$DOTHS")
        if [ -f $PROJECT/$subdir/$subdir$DOTHS ]; then

            # echo
            # echo -e "${PRE}MAKING $HSSUFF FROM $DOTHS"
            make rm -s
            make -s > /dev/null 2>&1 # do not print messy output from makefile
            make clean -s
            # echo -e "${PRE}MADE"

            output=$($PROJECT/$subdir/$subdir$HSSUFF) #should check output against value, get this from README
            
            make rm -s

            echo -ne " "$filebasename
            echo -ne "="$output
        fi
        cd $TESTHOME
    fi
    echo
done
echo -e "${PRE}COMPLETE"