#!/bin/bash

set -e

# Change directories into /people
cd ../people

# Look for README file
TARGET_FILE="README.md"

# Loop through directories to find target file
for dir in $( find . -type d );
do
  if [ -f "$dir/$TARGET_FILE" ]; then
    # echo "$dir/$TARGET_FILE";
    NAME=`head -n 1 "$dir/$TARGET_FILE"`;
    echo $NAME;
  fi
done
