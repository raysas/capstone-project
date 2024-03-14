#!/bin/bash

#this script is to automate roary's workflow for a set of genomes of the same species:
#1. runs prokka's annotation on all the genomes
#2. runs roary on the annotated genomes

#usage: bash create_pangenome.sh <path_to_genomes> <genus> <output_dir>
#test it: bash create_pangenome.sh data/genomes/Acinetobacter_baumannii/ Acinetobacer data/pangenomes/Acinetobacter/

path_to_genomes=$1 #if it ends with / trim it
if [ "${path_to_genomes: -1}" == "/" ]
then
    path_to_genomes="${path_to_genomes%/}"
fi

genus=$2

output_dir=$3 #check if it ends with / and remove it
if [ "${output_dir: -1}" == "/" ]
then
    output_dir="${output_dir%/}"
fi

gff_dir=$output_dir/gff_files/
log=$output_dir/output.log

echo "$path_to_genomes $output_dir"

if [ ! -f $log ]; then
    touch $log
    echo ">>>>>>>>>>>>>>>>> Created log file: $log" >> $log
else
    echo ">>>>>>>>>>>>>>>>> Log file already exists: $log; another run of the pipeline:" >> $log
fi

echo "" >> $log
echo "" >> $log

echo "---------------------------------------------------------------------------------------------------------" >> $log
echo ">>>>>>>>>>>>>>>>> Running create_pangenome.sh: the pangenome pipleline using prokka and roary" >> $log
echo "---------------------------------------------------------------------------------------------------------" >> $log
echo "---------------------------------------------------------------------------------------------------------" >> $log

if [ ! -d $output_dir ]; then
    mkdir $output_dir
    echo ">>>>>>>>>>>>>>>>> Created output directory for pangenome analysis: $output_dir" >> $log
else
    echo ">>>>>>>>>>>>>>>>> Output directory for pangenome analysis already exists: $output_dir" >> $log
fi

echo "---------------------------------------------------------------------------------------------------------" >> $log
echo "" >> $log

if [ ! -d $gff_dir ]; then
    #1. runs prokka's annotation on all the genomes
    echo "---------------------------------------------------------------------------------------------------------" >> $log
    echo ">>>>>>>>>>>>>>>>> Running prokka's annotation on all the genomes" >> $log
    echo "---------------------------------------------------------------------------------------------------------" >> $log
    echo "" >> $log

    for file in $path_to_genomes/*
    do 
        if [[ $file == *.fna ]]; then
            file_name=$(basename "$file" .fna)
            echo ">>>>>>>>>>>>>>>>> fna file: $file_name"

            this_gff=$output_dir/prokka_output/$file_name/$file_name.gff
            if [ ! -f $this_gff ]; then
                prokka --outdir $output_dir/prokka_output/$file_name/ --force --genus $genus --prefix $file_name $file 
                echo ">>>>>>>>>>>>>>>>> Annotated $file_name successfully: $output_dir/prokka_output/$file_name/" >> $log
            else
                echo ">>>>>>>>>>>>>>>>> $file_name already annotated" >> $log
            fi
        fi
    done
else
    echo "---------------------------------------------------------------------------------------------------------" >> $log
    echo ">>>>>>>>>>>>>>>>> GFF directory already exists: $gff_dir" >> $log
    echo "---------------------------------------------------------------------------------------------------------" >> $log
fi

#moving the gff files to the output directory
echo "" >> $log
echo "---------------------------------------------------------------------------------------------------------" >> $log

for dir in $output_dir/prokka_output/*/
do
    my_file=$(basename $dir /)
    my_file_relative_path=$dir$my_file.gff

    if [ ! -d $gff_dir ]; then
        mkdir $gff_dir
        echo ">>>>>>>>>>>>>>>>> Created gff directory: $gff_dir" >> $log
        echo "" >> $log
    fi

    echo ">>>>>>>>>>>>>>>>> moving $my_file_relative_path to $gff_dir"
    cp $my_file_relative_path $gff_dir
done

echo "" >> $log
echo "---------------------------------------------------------------------------------------------------------" >> $log
echo ">>>>>>>>>>>>>>>>> Moving the gff files to $gff_dir" >> $log
echo "---------------------------------------------------------------------------------------------------------" >> $log
echo "" >> $log

rm -r $output_dir/prokka_output

#2. runs roary on the annotated genomes

echo "---------------------------------------------------------------------------------------------------------" >> $log
echo ">>>>>>>>>>>>>>>>> Running roary on the annotated genomes" >> $log
echo "---------------------------------------------------------------------------------------------------------" >> $log
echo "" >> $log

roary_output=$output_dir/roary_pangenome
# roary -p 8 -f $roary_output $gff_dir/*.gff

echo "---------------------------------------------------------------------------------------------------------" >> $log
echo ">>>>>>>>>>>>>>>>> Pangenome created successfully: $roary_output" >> $log
echo "---------------------------------------------------------------------------------------------------------" >> $log