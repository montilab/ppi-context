def merge_dicts(dicts):
    merge = {}
    for d in dicts:
        for k,v in d.items():
            try:
                merge[k] += v
            except KeyError:
                merge[k] = v
            merge[k] = list(set(merge[k]))
    return merge

def split_ids(ids):
    pids = [j.lstrip('pubmed:') for j in ids.split('|')]
    return pids

def make_entry(**kwargs):
    return {k:v for k,v in kwargs.items()}
