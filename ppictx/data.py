import os
from urllib.request import urlretrieve

# Downloading raw data
URL_HIPPIE      = 'http://cbdm-01.zdv.uni-mainz.de/~mschaefer/hippie/HIPPIE-current.mitab.txt'
URL_PUBTATOR    = 'ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/cellline2pubtatorcentral.gz'
URL_CELLOSAURUS = 'ftp://ftp.expasy.org/databases/cellosaurus/cellosaurus.txt'

def download_data():
    dir = os.path.join(os.getcwd(), 'data-raw')
    
    if not os.path.exists(dir):
        os.makedirs(dir)

    fh = os.path.join(dir, 'HIPPIE.mitab')
    fp = os.path.join(dir, 'PUBTATOR.gz')
    fc = os.path.join(dir, 'CELLOSAURUS.txt')

    print('| Downloading raw data', end='')
    urlretrieve(URL_HIPPIE, fh)
    print('.', end='')
    urlretrieve(URL_PUBTATOR, fp)
    print('.', end='')
    urlretrieve(URL_CELLOSAURUS, fc)
    print('.')
    
    return(fh, fp, fc)
