'''
takes the DatasetS1 json file and makes a file of accession ids for each species
'''

import json
import os
import requests

DATA_DIR="data/"


def main():

    if not os.path.exists(f'{DATA_DIR}PATRIC_IDs'):
        os.makedirs(f'{DATA_DIR}PATRIC_IDs')

    #downloading json from supp info
    if not os.path.exists(f'{DATA_DIR}DatasetS1.json'):
        link="https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-023-43549-9/MediaObjects/41467_2023_43549_MOESM4_ESM.zip"
        r = requests.get(link)
        with open(f'{DATA_DIR}DatasetS1.zip','wb') as f:
            f.write(r.content)
        os.system('unzip {DATA_DIR}DatasetS1.zip -d {DATA_DIR}')

    with open(f'{DATA_DIR}DatasetS1.json','r') as f:
        json_data = json.load(f)

    for species in json_data:
        file_name=species.replace(' ','_')
        new_f=open(f'{DATA_DIR}PATRIC_IDs/{file_name}.txt','w')
        file_data="\n".join(json_data[species])
        file_data.strip()
        new_f.write(file_data)
        new_f.close()    

if __name__=='__main__':
    main()