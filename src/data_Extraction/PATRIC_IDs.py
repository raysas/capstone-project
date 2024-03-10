'''
takes the DatasetS1 json file and makes a file of accession ids for each specie
'''

import json

def main():
    with open('data/DatasetS1.json','r') as f:
        json_data = json.load(f)

    for species in json_data:
        file_name=species.replace(' ','_')
        new_f=open(f'data/PATRIC_IDs/{file_name}.txt','w')
        file_data="\n".join(json_data[species])
        file_data.strip()
        new_f.write(file_data)
        new_f.close()    

if __name__=='__main__':
    main()