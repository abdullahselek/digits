#!/bin/bash

cd "digits"
DATASET="dataset"
rm -rf "$DATASET" 
mkdir "$DATASET"
cd "$DATASET"

URL="http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
echo "Downloading from $URL"
curl "$URL" --output "${URL##*/}"
echo "${URL##*/} downloaded"

URL="http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz"
echo "Downloading from $URL"
curl "$URL" --output "${URL##*/}"
echo "${URL##*/} downloaded"

URL="http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz"
echo "Downloading from $URL"
curl "$URL" --output "${URL##*/}"
echo "${URL##*/} downloaded"

URL="http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"
echo "Downloading from $URL"
curl "$URL" --output "${URL##*/}"
echo "${URL##*/} downloaded"

# unzip all zipped files
gzip -d *.gz
rm -rf *.gz
