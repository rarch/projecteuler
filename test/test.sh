#!/bin/bash
# will test all project euler problems and makefiles
PROJECT=$PWD/".."
TEST=$PROJECT/"test"
PROBS=434

EXTENSIONS=( "py" "rb" )
DOTHS=".hs"

HSSUFF="_hs.out"
MAKEFILE="Makefile"

directories=()

echo "getting directory list"
# go through all project euler problems 1..434, convert number to string
for i in $(seq 1 $PROBS)
do
    subdir=$($TEST/numword.py $i)
    if [ -d $PROJECT/$subdir ]; then
        directories+=("$subdir")
    fi
done
echo "got directory list"

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

    if [ -f $PROJECT/$subdir/$MAKEFILE ]; then
        cd $PROJECT/$subdir

        filebasename=$(basename "$PROJECT/$subdir/$subdir$DOTHS")
        if [ -f $PROJECT/$subdir/$subdir$DOTHS ]; then

            echo
            make rm -s
            make -s
            make clean -s

            output=$($PROJECT/$subdir/$subdir$HSSUFF) #should check output against value, get this from README
            
            make rm -s

            echo -ne " "$filebasename
            echo -ne "="$output
        fi
        cd $TEST
    fi
    echo
done