import gzip
import pandas as pd

from Bio.ExPASy import cellosaurus

def process_ppi(fh):
    print('  ~ [PPI]')

    # Extract relevant information
    df = pd.read_csv(fh, sep='\t', header=0)
    df = df[['Gene Name Interactor A', 'Gene Name Interactor B', 'Publication Identifiers']]
    df.columns = ['gene_a', 'gene_b', 'ids']
    
    return(df)

def process_pid_cla(fp):
    print('  ~ [PID -> CLA]')

    # Create a table to match pid to one or more cla
    data = {}
    with gzip.open(fp, 'rb') as infile:
        for i, line in enumerate(infile):
            splat = str(line, 'utf-8').split('\t')
            pid = splat[0]
            cla = splat[2]
            try:
                data[pid].append(cla)
            except KeyError:
                data[pid] = [cla]

    return(data)

def process_cla_cid(fc):
    print('  ~ [CLA -> CID]')
    
    # Create a table to match cla to cid and associated cell line information
    data = {}
    with open(fc, 'r') as handle:
        records = cellosaurus.parse(handle)
        for i, record in enumerate(records):
            data[record['AC']] = {'ID': record['ID'], 
                                  'CA': record['CA'],
                                  'SX': record['SX'],
                                  'OX': [j.split(' ! ')[1] for j in record['OX']][0]}
    
    return(data)