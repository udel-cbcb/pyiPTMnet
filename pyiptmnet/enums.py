"""
Contains all the models required by the application
"""
from enum import Enum

class API_VERSION(Enum):
    V1 = "v1"

class Termtype(Enum):
    ALL = "All"
    UniprotID = "UniprotID"
    ProteinGeneName = "Protein/Gene Name"
    PMID = "PMID"


class PtmTypes(Enum):
    Acetylation="Acetylation"
    CGlycosylation="C-Glycosylation"
    Myristoylation="Myristoylation"
    Ubiquitination="Ubiquitination"
    NGlycosylation="N-Glycosylation"
    SGlycosylation="S-Glycosylation"
    Phosphorylation="Phosphorylation"
    SNitrosylation="S-Nitrosylation"
    OGlycosylation="O-Glycosylation"
    Methylation="Methylation"
    Sumoylation="Sumoylation"


class Role(Enum):
    EnzymeOrSubstrate = "Enzyme or Substrate"
    Enzyme = "Enzyme"
    Substrate = "Substrate"
    EnzymeAndSubstrate = "Enzyme and Substrate"


class Organism:

    schema = {
        "type" : ["object","null"],
        "properties": {
            "taxon_code": {"type":"number"},
            "protein_name":{"type":"string"},
            "gene_name":{"type":"string"},
        }
    }


class SearchResult:

    schema = {
        "type" : "object",
        "properties": {
            "iptm_id": {"type":"string"},
            "protein_name": {"type":"string"},
            "gene_name": {"type":"string"},
            "synonyms": {"type": "array","items":{"type":"string"}},
            "organism":Organism.schema,
            "substrate_role": {"type":"boolean"},
            "substrate_num": {"type":"number"},
            "enzyme_role": {"type":"boolean"},
            "ptm_dependent_ppi_role": {"type":"boolean"},
            "ptm_dependent_ppi_num": {"type":"number"},
            "sites": {"type":"number"},
            "isoforms": {"type":"number"}
        }
    }


class Pro:

    schema = {
        "type" : "object",
        "properties": {
            "id": {"type":"string"},
            "name": {"type":"string"},
            "definition": {"type":"string"},
            "short_label": {"type": "string"},
            "category": {"type": "string"},
        }
    }


class Info:

    schema = {
        "type" : "object",
        "properties": {
            "uniprot_ac": {"type":"string"},
            "uniprot_id": {"type":"string"},
            "protein_name": {"type":"string"},
            "gene_name": {"type": "string"},
            "synonyms": {"type": "array","items":{"type":"string"}},
            "organism":Organism.schema,
            "pro": Pro.schema,
        }
    }


class ProEntity:
    schema = {
        "type": "object",
        "properties": {
            "pro_id": {"type": "string"},
            "label": {"type": "string"}
        }
    }


class Source:
    schema = {
        "type": "object",
        "properties": {
            "label": {"type": "string"},
            "name": {"type": "string"},
            "url": {"type": "string"}
        }
    }


class Proteoform:
    schema = {
        "type" : "object",
        "properties": {
            "pro_id": {"type":"string"},
            "label": {"type":"string"},
            "sites": {"type": "array","items":{"type":"string"}},
            "ptm_enzyme": ProEntity.schema,
            "source": Source.schema,
        }
    }


class Entity:

    schema = {
        "type" : "object",
        "properties": {
            "uniprot_id": {"type":"string"},
            "name":{"type":"string"}
        }
    }


class PTMPPI:

    schema = {
        "type" : "object",
        "properties": {
            "ptm_type": {"type":"string"},
            "substrate":Entity.schema,
            "site":{"type":"string"},
            "interactant": Entity.schema,
            "association_type": {"type": "string"},
            "source": Source.schema,
            "pmid": {"type": "string"}
        }
    }


class ProteoformPPI:

    schema = {
        "type": "object",
        "properties": {
            "protein_1": ProEntity.schema,
            "relation": {"type":"string"},
            "protein_2": ProEntity.schema,
            "pmids": {"type": "array","items":{"type":"string"}}
        }
    }


class QuerySubstrate:

    schema = {
        "type" : "object",
        "properties": {
            "substrate_ac": {"type":"string"},
            "site_residue":{"type":"string"},
            "site_position":{"type":"string"}
        }
    }


class BatchPTMEnzyme:

    schema = {
        "type": "object",
        "properties": {
            "ptm_type": {"type": "string"},
            "substrate": Entity.schema,
            "site": {"type": "string"},
            "site_position": {"type": "number"},
            "ptm_enzyme": Entity.schema,
            "score": {"type": "number"},
            "source": {"type": "array","items":Source.schema},
            "pmids": {"type": "array","items":{"type":"string"}}
        }
    }


class BatchPTMPPI:

    schema = {
        "type": "object",
        "properties": {
            "ptm_type": {"type": "string"},
            "substrate": Entity.schema,
            "site": {"type": "string"},
            "site_position": {"type": "number"},
            "interactant": Entity.schema,
            "association_type": {"type": "string"},
            "source": Source.schema,
            "pmids": {"type": "array","items":{"type":"string"}}
        }
    }
