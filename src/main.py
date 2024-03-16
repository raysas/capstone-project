import data_utils
import network_calculations

def main():
    PHENO_PATH='data/phenotypes/Campylobacter_coli_ciprofloxacin.csv'
    SPECIES_IDS_PATH='data/PATRIC_IDs/Campylobacter_coli.txt'
    PRESENCE_MATRIX_PATH='data/pangenomes/Campylobacter_coli/roary_pangenome/gene_presence_absence.Rtab'

    df=network_calculations.log_odds(PHENO_PATH, SPECIES_IDS_PATH, PRESENCE_MATRIX_PATH, remove_hypothetical=False)
    df.to_csv('data/processed/log_odds/Campylobacter_coli_ciprofloxacin.csv')

if __name__ == "__main__":
    main()