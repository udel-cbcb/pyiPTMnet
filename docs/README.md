## pyIPTMnet

> A simple and lightweight client library for iPTMnet.

## What is it

pyIPTMnet is a thin wrapper around the rest api for the iPTMnet database. It makes it very easy to query the iPTMnet database and integrate the results into existing bioinformatics pipeline.    

See the [Quick start](quickstart.md) for more details.

## Installation
```
pip install pyiptmnet
```

# Quick start

The API consists of functions that mirror the functionality of the iPTMNet rest api.

## Info
Retriving information for an entry with an iPTMnet ID - `Q15796`
``` python
# imports
import iptmnet.api as api
import * from iptmnet.enums

# get the information for Q15796 
iptmnet.api.get_info("Q15796")
```

##### Result
Type : `dictionary`
``` json
{
  "uniprot_ac": "Q15796",
  "uniprot_id": "SMAD2_HUMAN",
  "protein_name": "Mothers against decapentaplegic homolog 2;",
  "gene_name": "SMAD2",
  "synonyms": [
    "MADH2",
    "MADR2"
  ],
  "organism": {
    "taxon_code": 9606,
    "species": "Homo sapiens",
    "common_name": "Human"
  },
  "pro": {
    "id": "PR:Q15796",
    "name": "mothers against decapentaplegic homolog 2 (human)",
    "definition": "A smad2 that is encoded in the genome of human.",
    "short_label": "hSMAD2",
    "category": "organism-gene"
  }
}
```


## Search
To search the iPTMnet database for entries related to the gene `smad2`, you can use the `search` function as follows.

``` python
# imports
import iptmnet.api as api
import * from iptmnet.enums

# search the database
iptmnet.api.search("smad2", Termtype.ProteinGeneName, Role.EnzymeOrSubstrate)
```

##### Result 
Type : `dataframe`

iptm_id | protein_name | gene_name | synonyms | organism_taxon_code | organism_species | organism_common_name | substrate_role | substrate_num | enzyme_role | enzyme_num | ptm_dependent_ppi_role | ptm_dep_ppi_num | sites | isoforms
--- | --- | ---  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- 
O70436 | Mothers against decapentaplegic homolog 2; | Smad2 | Madh2 | 10116 | Rattus norvegicus | Rat | True | 0 | False | 0 | False | 0 | 6 | 0
Q1W668 | Mothers against decapentaplegic homolog 2; | SMAD2 |  | 9913 | Bos taurus | Bovine | True | 0 | False | 0 | False | 0 | 4 | 0

## Bulk
To perform a bulk query for ptm enzymes on the database with a list of PTM sites in a csv file - `sites.csv` you can use `get_ptm_enzymes_from_file` function.

``` python
# imports
import iptmnet.api as api
import * from iptmnet.enums

# search the database
iptmnet.api.get_ptm_enzymes_from_file("sites.csv")
```
##### Result 
Type : `dataframe`

ptm_type | site | site_position | score | source | pmid | enz_name | enz_id | sub_name | sub_id |
--- | --- | ---  | --- | --- | --- | --- | --- | --- | ---  
Phosphorylation | S2 | 2 | 2 | HPRD | 8898866,20068231 | PRKCB | P05771 | ANXA2 | P07355 
Phosphorylation | S7 | 7 | 4 | HPRD,neXtPro | 20166139,12773393,20089855,17924679,11438671 | RPS6KA5 | O75582 | HMGN1 | P05114 
Phosphorylation | T60 | 60 | 4 | neXtProt,PSP | 21355052,16081417 | SGK1 | O00141 | WNK1 | Q9H4A3