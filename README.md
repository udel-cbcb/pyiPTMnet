
> A simple and lightweight client library for iPTMnet.

## What is it

pyiPTMnet is a thin wrapper around the rest api of iPTMnet database. It makes it very easy to query iPTMnet database and integrate the results into any existing bioinformatics pipeline.    

## Installation

***Please not this package is only available for python 3.0+***

#### Install from PyPI
``` Python
pip install pyiptmnet
```

#### Install from Github
``` bash
pip install git+https://github.com/udel-cbcb/pyiptmnet.git#egg=pyiptmnet
```

# Quick start

The API consists of functions that mirror the functionality of the iPTMNet rest api. Below you can find a few examples of the functions provided by the API.

## Info
Retriving information for an entry with an iPTMnet ID - `Q15796`
``` python
#imports
import pyiptmnet.api as api

# get the information for Q15796 
api.get_info("Q15796")
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
#imports
import pyiptmnet.api as api
from pyiptmnet.enums import *

# search the database
api.search("smad2", Termtype.ProteinGeneName, Role.EnzymeOrSubstrate)
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
#imports
import pyiptmnet.api as api
from pyiptmnet.enums import *

# search the database
api.get_ptm_enzymes_from_file("sites.csv")
```

##### Result 
Type : `dataframe`

ptm_type | site | site_position | score | source | pmid | enz_name | enz_id | sub_name | sub_id |
--- | --- | ---  | --- | --- | --- | --- | --- | --- | ---  
Phosphorylation | S2 | 2 | 2 | HPRD | 8898866,20068231 | PRKCB | P05771 | ANXA2 | P07355 
Phosphorylation | S7 | 7 | 4 | HPRD,neXtPro | 20166139,12773393,20089855,17924679,11438671 | RPS6KA5 | O75582 | HMGN1 | P05114 
Phosphorylation | T60 | 60 | 4 | neXtProt,PSP | 21355052,16081417 | SGK1 | O00141 | WNK1 | Q9H4A3

#### Running tests

```
python -m unittest test.tests
```

#### Citation
If you like our work and it helps you in your research, please cite us using the following citation.

```
@article{10.1093/database/baz157,
    author = {Gavali, Sachin and Cowart, Julie and Chen, Chuming and Ross, Karen E and Arighi, Cecilia and Wu, Cathy H},
    title = "{RESTful API for iPTMnet: a resource for protein post-translational modification network discovery}",
    journal = {Database},
    volume = {2020},
    year = {2020},
    month = {05},
    abstract = "{iPTMnet is a bioinformatics resource that integrates protein post-translational modification (PTM) data from text mining and curated databases and ontologies to aid in knowledge discovery and scientific study. The current iPTMnet website can be used for querying and browsing rich PTM information but does not support automated iPTMnet data integration with other tools. Hence, we have developed a RESTful API utilizing the latest developments in cloud technologies to facilitate the integration of iPTMnet into existing tools and pipelines. We have packaged iPTMnet API software in Docker containers and published it on DockerHub for easy redistribution. We have also developed Python and R packages that allow users to integrate iPTMnet for scientific discovery, as demonstrated in a use case that connects PTM sites to kinase signaling pathways.}",
    issn = {1758-0463},
    doi = {10.1093/database/baz157},
    url = {https://doi.org/10.1093/database/baz157},
    note = {baz157},
    eprint = {https://academic.oup.com/database/article-pdf/doi/10.1093/database/baz157/33205374/baz157.pdf},
}
```


## Citations of the underlying Sources
| \# | Name            | Publication                                                                                                                                                                                                                                                                                                                                                                                            | PubMed   |
|----|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 1  | HPRD            | Prasad, T\. S\. K\. et al\. \(2009\) Human Protein Reference Database \- 2009 Update\. Nucleic Acids Research\. 37, D767\-72\.                                                                                                                                                                                                                                                                         | 18988627 |
| 2  | phospho\.ELM    | Dinkel H, Chica C, Via A, Gould CM, Jensen LJ, Gibson TJ, Diella F\. Nucleic Acids Res\. 2011 Jan;39\(Database issue\) 261\-7\. doi: 10\.1093/nar/gkq1104\.                                                                                                                                                                                                                                            | 21062810 |
| 3  | p3DB            | 	Yao Q, Ge H, Wu S, Zhang N, Chen W, Xu C, Gao J, Thelen JJ, Xu D\. \(2013\) P3DB 3\.0: From plant phosphorylation sites to protein networks\. Nucleic Acids Res 2013\. 42\(Database issue\):D1206\-D1213                                                                                                                                                                                              | 24243849 |
| 4  | PhosphoGrid     | Stark C, Breitkreutz BJ, Reguly T, Boucher L, Breitkreutz A, Tyers M\. Biogrid: A General Repository for Interaction Datasets\. Nucleic Acids Res\. 2006; 34:D535\-9\.                                                                                                                                                                                                                                 | 16381927 |
| 5  | PomBase         | Wood V, Harris MA, McDowall MD, Rutherford K, Vaughan BW, Staines DM, Aslett M, Lock A, Bähler J, Kersey PJ, Oliver SG\. PomBase: a comprehensive online resource for fission yeast\. Nucleic Acids Res\. 2012;40\(Database issue\):D695\-9\. Epub 2011                                                                                                                                                | 22039153 |
| 6  | neXtProt        | Gaudet P, Michel PA, Zahn\-Zabal M, Britan A, Cusin I, Domagalski M, Duek PD, Gateau A, Gleizes A, Hinard V, Rech de Laval V, Lin JJ, Nikitin F, Schaeffer M, Teixeira D, Lane L, Bairoch A\. The neXtProt knowledgebase on human proteins: 2017 update\. Nucleic Acids Res\. 2017; 45\(D1\):D177\-D182 doi:10\.1093/nar/gkw1062                                                                       | 27899619 |
| 7  | Signor          | Perfetto L, Briganti L, Calderone A, Cerquone Perpetuini A, Iannuccelli M, Langone F, Licata L, Marinkovic M, Mattioni A, Pavlidou T, Peluso D, Petrilli LL, Pirrò S, Posca D, Santonico E, Silvestri A, Spada F, Castagnoli L, Cesareni G\. SIGNOR: a database of causal relationships between biological entities\. Nucleic Acids Res\. 2016;44\(D1\):D548\-54\. doi: 10\.1093/nar/gkv1048           | 26467481 |
| 8  | dbSNO           | Chen YJ, Lu CT, Su MG, Huang KY, Ching WC, Yang HH, Liao YC, Chen YJ, Lee TY\. dbSNO 2\.0: a resource for exploring structural environment, functional and disease association and regulatory network of protein S\-nitrosylation\. Nucleic Acids Res\. 2015;43\(Database issue\):D503\-11\. doi: 10\.1093/nar/gku1176\.                                                                               | 25399423 |
| 9  | PhosphoSitePlus | Hornbeck PV, Zhang B, Murray B, Kornhauser JM, Latham V, Skrzypek E\. PhosphoSitePlus, 2014: mutations, PTMs and recalibrations\. Nucleic Acids Res\. 2015;43\(Database issue\):D512\-20\. doi: 10\.1093/nar/gku1267\.                                                                                                                                                                                 | 25514926 |
| 10 | PhosPhAt        | 	Durek P, Schmidt R, Heazlewood JL, Jones A, Maclean D, Nagel A, Kersten B, Schulze WX\. PhosPhAt: the Arabidopsis thaliana phosphorylation site database\. An update\. Nucleic Acids Res\. 38: D828\-D834 \(2010\)                                                                                                                                                                                    | 17984086 |
| 11 | UniProt         | The UniProt Consortium\. UniProt: the universal protein knowledgebase Nucleic Acids Res\. 45: D158\-D169 \(2017\)                                                                                                                                                                                                                                                                                      | 27899622 |
| 12 | PRO             | Natale DA, Arighi CN, Blake JA, Bona J, Chen C, Chen SC, Christie KR, Cowart J, D'Eustachio P, Diehl AD, Drabkin HJ, Duncan WD, Huang H, Ren J, Ross K,Ruttenberg A, Shamovsky V, Smith B, Wang Q, Zhang J, El\-Sayed A, Wu CH\. Protein Ontology \(PRO\): enhancing and scaling up the representation of protein entities\. Nucleic Acids Res\.2017;45\(D1\):D339\-D346\. doi: 10\.1093/nar/gkw1075\. | 27899649 |
| 13 | RLIMS\-P        | Torii M, Li G, Li Z, Oughtred R, Diella F, Celen I, Arighi CN, Huang H, Vijay\-Shanker K, Wu CH\. RLIMS\-P: an online text\-mining tool for literature\-based extraction of protein phosphorylation information\. Database \(Oxford\)\.2014\. pii: bau081\. doi: 10\.1093/database/bau081\.                                                                                                            | 25122463 |
| 14 | eFIP            | Wang Q, Ross KE, Huang H, Ren J, Li G, Vijay\-Shanker K, Wu CH, Arighi CN\. Analysis of Protein Phosphorylation and Its Functional Impact on Protein\-Protein Interactions via Text Mining of the Scientific Literature\. Methods Mol Biol\. 2017;1558:213\-232\. doi: 10\.1007/978\-1\-4939\-6783\-4\_10\.                                                                                            | 28150240 |
| 15 | SGD             | Paskov KM, Wong ED, Karra K, Engel SR, Cherry JM\. Curated protein information in the Saccharomyces genome database\. Database \(Oxford\)\. 2017 Jan 1;2017\(1\)\. doi: 10\.1093/database/bax011                                                                                                                                                                                                       | 28365727 |
| 16 | Biomuta         | Dingerdissen HM, Torcivia\-Rodriguez J, Hu Y, Chang TC, Mazumder R, Kahsay R\. BioMuta and BioXpress: mutation and expression knowledgebases for cancerbiomarker discovery\. Nucleic Acids Res\. 2018 Jan 4;46\(D1\):D1128\-D1136\. doi:10\.1093/nar/gkx907                                                                                                                                            | 30053270 |
