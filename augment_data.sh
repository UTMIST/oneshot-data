#!/bin/sh

source_directory="./omniglot/python/$1.zip"
target_directory="./data/$1"

echo $source_directory
echo $target_directory

if test -f $source_directory; then
    cp $source_directory "$target_directory.zip"
else
    echo "File not found"
    exit -1
fi

# unzip "$target_directory.zip"
# echo "Hello"
# rm "$target_directory.zip"

# python data_aug/aug.py

zip "$1.zip" -r $target_directory
