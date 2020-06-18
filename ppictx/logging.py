import itertools
import ppictx

def logging_ppi_cid(df, logs):
    ppis_processed = logs
    pids_found = [list(i.keys()) for i in ppis_processed if len(i.keys()) > 0]
    pids_unique = set(itertools.chain.from_iterable(pids_found))

    pids_processed = ppictx.merge_dicts(logs)
    clas_found = [v for k,v in pids_processed.items() if len(v) > 0]
    clas_unique = set(itertools.chain.from_iterable(clas_found))

    print('| Mapping')
    print('  ~ Processed {} original PPIs'.format(len(ppis_processed)))
    print('  ~ Found {} unique PIDs for {} / {} PPIs ({:.2f}%)'.format(len(pids_unique), 
                                                                       len(pids_found), 
                                                                       len(ppis_processed), 
                                                                       len(pids_found)/len(ppis_processed)*100))

    print('  ~ Found {} unique CLAs for {} / {} PIDs ({:.2f}%)'.format(len(clas_unique), 
                                                                       len(clas_found), 
                                                                       len(pids_processed.items()), 
                                                                       len(clas_found)/len(pids_processed.items())*100))
    print('| Results')
    print('  ~ {} PPIs contextualized with {} unique CIDs from {} original PPIs'.format(df.shape[0],
                                                                                        df['cell_name'].nunique(),
                                                                                        df['id'].nunique()))