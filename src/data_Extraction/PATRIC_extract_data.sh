#!/bin/sh

if [ ! -f "data/genome_summary.csv" ]; then
    curl ftp://ftp.bvbrc.org/RELEASE_NOTES/genome_summary -o data/genome_summary.tsv
    sed 's/\t/,/g' data/genome_summary.csv > data/genome_summary.csv
    rm -f data/genome_summary.tsv
fi  

python src/data_Extraction/PATRIC_IDs.py 

for file in `ls data/PATRIC_IDs/`;do

    dir_name=$(basename -s .txt $file)
    dir_path=data/genomes/$dir_name/

    # if [ ! -d ]
    mkdir $dir_path

    for i in `cat data/PATRIC_IDs/$file`; do 
        curl -s -o ${dir_path}${i}.fna "ftp://ftp.bvbrc.org/genomes/$i/$i.fna";
        echo $i
    done

    echo "- Downloaded genomes from $file accession IDs"
done