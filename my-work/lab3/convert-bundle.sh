#!/bin/bash

#Define variables:
URL="https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz"
TARBALL="lab3-bundle.tar.gz"

# Fetch tarball
curl -o $TARBALL $URL

# Decompress archive
tar -xzvf $TARBALL

# Remove spaces
# awk '!/^[[:space:]]*$/' myfile.tsv > file.tsv
cat lab3_data.tsv | tr -s '\n' > new-lab3-data.tsv

# Convert to .csv
tr '\t' ',' < new-lab3-data.tsv > lab3-data.csv

# Count lines of data
LINES=$(wc -l < lab3-data.csv)
COUNT=$(($LINES - 1))
echo $COUNT

# Create new tarball
tar -czvf converted-archive.tar.gz lab3-data.csv

# Remove uneccesary files
rm lab3_data.tsv new-lab3-data.tsv lab3-bundle.tar.gz

