import os
import itertools
import pandas as pd
import ppictx

def process_ppi_cid(ppi, pid_cla, cla_cid):
    print('  ~ [PPI -> PID -> CLA -> CID]')

    # Storage
    logs = []
    data = []

    # For each interaction
    for i, row in ppi.iterrows():
        log = {}
        gene_a, gene_b, ids = row['gene_a'], row['gene_b'], row['ids']
        
        # Check if publications exist
        if ids != '-':

            # For each publication reporting this interaction
            pids = ppictx.split_ids(ids)
            for pid in pids:
                log[pid] = {}
                try:
                    # Check for extracted cell lines
                    clas = pid_cla[pid]
                    log[pid] = clas

                    # For each cell line extracted from the study
                    for cla in clas:
                        try:
                            cid = cla_cid[cla]
                            data.append(ppictx.make_entry(id=i, 
                                                          gene_a=gene_a, 
                                                          gene_b=gene_b, 
                                                          pid=pid, 
                                                          cell_name=cid['ID'], 
                                                          cell_category=cid['CA'],
                                                          cell_sex=cid['SX'],
                                                          cell_species=cid['OX']))

                        except KeyError as e:
                            pass

                except KeyError:
                    pass

        logs.append(log)

    # Save data
    dir = os.path.join(os.getcwd(), 'data')
    if not os.path.exists(dir):
        os.makedirs(dir)
    df_context = pd.DataFrame(data)
    df_context = df_context[['id', 'gene_a', 'gene_b', 'pid', 'cell_name', 'cell_category', 'cell_sex', 'cell_species']]
    df_context.to_csv(os.path.join(dir, 'PPI-Context.txt'), sep='\t', index=False)

    return df_context, logs

def process_raw_data(fh, fp, fc):
    print('| Processing raw data')
    ppi = ppictx.process_ppi(fh)
    pid_cla = ppictx.process_pid_cla(fp)
    cla_cid = ppictx.process_cla_cid(fc)
    df, logs = process_ppi_cid(ppi, pid_cla, cla_cid)
    ppictx.logging_ppi_cid(df, logs)
