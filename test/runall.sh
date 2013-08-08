#!/bin/bash

dir=".."
data=$dir"/data"
solutions=$dir"/solutions"
util=$dir"/util"

Extensions=( "py" "rb" )

control_c() {
    exit -1
}

trap control_c SIGINT

for subdir in $dir/*
do
    dirname=$(basename "$subdir")
    if [ -d $subdir ] && [ ! "$subdir" = "$data" ] \
        && [ ! "$subdir" = "$solutions" ] && [ ! "$subdir" = "$util" ]; then
        
        for file in $subdir/*
        do
            filebasename=$(basename "$file")
            ext="${filebasename##*.}"
            filename="${filebasename%.*}"

            if [ -x $file ]; then
                for acceptable in ${Extensions[@]}
                do
                    if [ "$ext" = "$acceptable" ] && [ "$filename" = "$dirname" ]; then
                        echo $file
                        $file
                    fi
                done
                # files without extension, compiled from haskell
                if [ "$ext" = "$filename" ] && [ "$filename" = "$dirname" ]; then
                    echo $file
                    $file
                fi

            fi
        done

    fi
done

exit 0

