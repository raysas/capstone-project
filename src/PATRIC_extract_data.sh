#!/bin/sh

if [ ! -f "data/genome_summary.csv" ]; then
    curl ftp://ftp.bvbrc.org/RELEASE_NOTES/genome_summary -o data/genome_summary.tsv
    sed 's/\t/,/g' data/genome_summary.csv > data/genome_summary.csv
fi  

csv_file='data/genome_summary.csv'
species_name="Stenotrophomonas maltophiliae"

contigs=$(awk -F ',' '{print $11}' $csv_file | tail -n +2)
genome_status=$(awk -F ',' '{print $4}' $csv_file | tail -n +2)
genome_length=$(awk -F ',' '{print $5}' $csv_file | tail -n +2)
patric_cds=$(awk -F ',' '{print $12}' $csv_file | tail -n +2)
genomes_name=$(awk -F ',' '{print $2}' $csv_file | tail -n +2)
genome_id=$(awk -F ',' '{print $1}' $csv_file | tail -n +2)

#getting statistics and lower/upper bounds
median_contigs=$(echo $contigs | tr ',' '\n' | sort -n | awk '{a[i++]=$1} END {print a[int(i/2)]}') #test it

mean_genome_length=$(echo $genome_length | tr ',' '\n' | awk '{sum+=$1} END {print sum/NR}') #test it
sd_genome_length=$(echo $genome_length | tr ',' '\n' | awk '{sum+=$1; sumsq+=$1*$1} END {print sqrt(sumsq/NR - (sum/NR)**2)}') #test it



#########################################
#SHOULD MAKE IT SPECIES SPECIFIC
#########################################
#########################################
#########################################
mean_cds=$(echo $patric_cds | tr ',' '\n' | awk '{sum+=$1} END {print sum/NR}') 
sd_cds=$(echo $patric_cds | tr ',' '\n' | awk '{sum+=$1; sumsq+=$1*$1} END {print sqrt(sumsq/NR - (sum/NR)**2)}')


echo "The median number of contigs for $species_name is $median_contigs"
echo "The mean genome length for $species_name is $mean_genome_length"
echo "The mean number of CDS for $species_name is $mean_cds"



contigs_lb=$median_contigs-2.5*$median_contigs
contigs_ub=$median_contigs+2.5*$median_contigs

genome_length_lb=$mean_genome_length-3*$sd_genome_length
genome_length_ub=$mean_genome_length+3*$sd_genome_length

cds_lb=$mean_cds-3*$sd_cds
cds_ub=$mean_cds+3*$sd_cds  


#for completness
completeness="Complete WGS"  
pattern=$(echo $completeness | sed 's/ /|/g') 


#filter one by one
species_filtered=$(awk -F ',' -v species_name="$species_name" '{if($2 ~ species_name) print $0}' $csv_file) 
echo "filtered by species" 
completeness_filtered=$(awk -F ',' -v pattern="$pattern" '{if($4 ~ pattern) print $0}' "$species_filtered")
echo "filtered by completeness"
contigs_filtered=$(awk -F ',' -v contigs_lb=$contigs_lb -v contigs_ub=$contigs_ub '{if($11>=contigs_lb && $11<=contigs_ub) print $0}' $completness_filtered) 
echo "filtered by contigs" 
length_filtered=$(awk -F ',' -v genome_length_lb=$genome_length_lb -v genome_length_ub=$genome_length_ub '{if($5>=genome_length_lb && $5<=genome_length_ub) print $0}' $contigs_filtered)
echo "filtered by length"
all_filtered=$(awk -F ',' -v cds_lb=$cds_lb -v cds_ub=$cds_ub '{if($12>=cds_lb && $12<=cds_ub) print $0}' $length_filtered) 

echo $all_filtered > data/filtered_genomes.csv
ids_filtered=$(echo $all_filtered | awk -F ',' '{print $1}' | tr ' ' '\n')
echo ids_filtered > data/filtered_genomes_ids.txt
