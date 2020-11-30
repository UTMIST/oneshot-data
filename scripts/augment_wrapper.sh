#!/bin/sh

sandbox_dir="./data_augmented"
if [ ! -e "$sandbox_dir" ]; then
    mkdir $sandbox_dir
fi

source_path="./omniglot/python/$1.zip"
target_path="$sandbox_dir/$1.zip"
target_dir="$sandbox_dir/$1"
result_dir="$sandbox_dir/$2"
result_path="$sandbox_dir/$2.zip"

if test -f $source_path; then
    cp $source_path "$target_path"
else
    echo "File not found"
    exit -1
fi

unzip "$target_path" -d "$sandbox_dir/"
python scripts/augment.py $1
mv $target_dir $result_dir
zip $result_path -r "$result_dir"
rm -rf $target_path $result_dir
