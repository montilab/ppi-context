
<!-- README.md is generated from README.Rmd. Please edit that file -->

# PPI-Context

Contextualization of protein-protein interaction databases by cell line

#### Clone repository

    git clone https://github.com/montilab/ppi-context
    cd ppi-context

#### The data

If you just want the data it’s easy to load into R…

``` r
ppi <- read.delim("data/PPI-Context.txt", header=TRUE, sep="\t", stringsAsFactors=FALSE)
head(ppi)
```

    #>   id  gene_a  gene_b      pid cell_name                        cell_category
    #> 1  0 ALDH1A1 ALDH1A1 25416956       HEK                     Cancer cell line
    #> 2  2 PPP1R9A   ACTG1  9362513      Rat1 Spontaneously immortalized cell line
    #> 3  2 PPP1R9A   ACTG1  9362513      PC12                     Cancer cell line
    #> 4  2 PPP1R9A   ACTG1  9362513       Sf9 Spontaneously immortalized cell line
    #> 5  2 PPP1R9A   ACTG1  9362513     COS-7                Transformed cell line
    #> 6  7  PIK3R2   ERBB2 16729043  Hs 912.T                     Cancer cell line
    #>   cell_sex          cell_species
    #> 1   Female          Homo sapiens
    #> 2              Rattus norvegicus
    #> 3     Male     Rattus norvegicus
    #> 4   Female Spodoptera frugiperda
    #> 5     Male  Chlorocebus aethiops
    #> 6   Female          Homo sapiens

#### Pre-processing the data

    | PPI - Context (v1.0)
    usage: pipeline.py [-h] [-r] [-d]
                       [-fh PATH_HIPPIE] 
                       [-fp PATH_PUBTATOR]
                       [-fc PATH_CELLOSAURUS]
    
    optional arguments:
      -h, --help            show this help message and exit
      -r, --run             run pipeline
      -d, --download        download raw data first
      -fh PATH_HIPPIE       path to downloaded Hippie data (optional)
      -fp PATH_PUBTATOR     path to downloaded Pubtator data (optional)
      -fc PATH_CELLOSAURUS  path to downloaded Cellosaurus data (optional)

In most cases you will need to download the latest bulk data first and
then process it…

``` bash
python3 ppictx.py --download --run
```

    | PPI - Context (v1.0)
    | Downloading raw data...
    | Processing raw data
      ~ [PPI]
      ~ [PID -> CLA]
      ~ [CLA -> CID]
      ~ [PPI -> PID -> CLA -> CID]

In other cases, you might have the previous versions of the data to
process…

``` bash
python3 ppictx.py --run \
                  -fh path/to/HIPPIE.mitab \
                  -fp path/to/PUBTATOR.gz \
                  -fc path/to/CELLOSAURUS.txt
```