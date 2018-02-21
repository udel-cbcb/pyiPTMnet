import json
import requests
import csv

def search(search_term, term_type,role,ptm_list=None,organism_list=None):
    if ptm_list is None:
        ptm_list = []
    else:
        # iterate the original list to create a new list with values
        ptm_value_list = []
        for ptm in ptm_list:
            ptm_value_list.append(ptm.value)

        # ptm_list = ptm_value_list
        ptm_list = ptm_value_list

    if organism_list is None:
        organism_list = []

    data = {
        "search_term":search_term,
        "term_type":term_type.value,
        "ptm_type":ptm_list,
        "role":role.value,
        "organism":organism_list
    }

    result = requests.get("https://annotation.dbi.udel.edu/iptmnet/api/search",params=data,verify=False)

    if result.status_code is 200:
        # read the result
        search_results = json.loads(result.text)
        return search_results
    else:
        # raise the error
        result.raise_for_status()


def get_info(id):
    url = "https://annotation.dbi.udel.edu/iptmnet/api/{id}/info".format(id=id)
    result = requests.get(url,verify=False)

    if result.status_code is 200:
        # read the result
        info = json.loads(result.text)
        return info
    else:
        # raise the error
        result.raise_for_status()


def get_msa(id):
    raise NotImplementedError


def get_substrates(id):
    url = "https://annotation.dbi.udel.edu/iptmnet/api/{id}/substrate".format(id=id)
    result = requests.get(url,verify=False)

    if result.status_code is 200:
        # read the result
        info = json.loads(result.text)
        return info
    else:
        # raise the error
        result.raise_for_status()


def get_proteoforms(id):
    url = "https://annotation.dbi.udel.edu/iptmnet/api/{id}/proteoforms".format(id=id)
    result = requests.get(url,verify=False)

    if result.status_code is 200:
        # read the result
        info = json.loads(result.text)
        return info
    else:
        # raise the error
        result.raise_for_status()


def get_ptm_dependent_ppi(id):
    url = "https://annotation.dbi.udel.edu/iptmnet/api/{id}/ptmppi".format(id=id)
    result = requests.get(url,verify=False)

    if result.status_code is 200:
        # read the result
        info = json.loads(result.text)
        return info
    else:
        # raise the error
        result.raise_for_status()


def get_ppi_for_proteoforms(id):
    url = "https://annotation.dbi.udel.edu/iptmnet/api/{id}/proteoformppi".format(id=id)
    result = requests.get(url,verify=False)

    if result.status_code is 200:
        # read the result
        info = json.loads(result.text)
        return info
    else:
        # raise the error
        result.raise_for_status()


def get_ptm_enzymes_from_file(file_name):
    substrates = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for substrate_ac,site_residue,site_position in reader:
            substrate = {
                "substrate_ac": substrate_ac,
                "site_residue": site_residue,
                "site_position": site_position
            }
            substrates.append(substrate)

    return get_ptm_enzymes_from_list(substrates)


def get_ptm_enzymes_from_list(items):
    url = "https://annotation.dbi.udel.edu/iptmnet/api/batch_ptm_enzymes"
    json_data = json.dumps(items,indent=4)
    result = requests.post(url,data=json_data,verify=False)

    if result.status_code is 200:
        # read the result
        info = json.loads(result.text)
        return info
    else:
        # raise the error
        result.raise_for_status()


def get_ptm_ppi_from_file(file_name):
    substrates = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for substrate_ac,site_residue,site_position in reader:
            substrate = {
                "substrate_ac": substrate_ac,
                "site_residue": site_residue,
                "site_position": site_position
            }
            substrates.append(substrate)

    return get_ptm_ppi_from_list(substrates)


def get_ptm_ppi_from_list(items):
    url = "https://annotation.dbi.udel.edu/iptmnet/api/batch_ptm_ppi"
    json_data = json.dumps(items,indent=4)
    result = requests.post(url,data=json_data,verify=False)

    if result.status_code is 200:
        # read the result
        info = json.loads(result.text)
        return info
    else:
        # raise the error
        result.raise_for_status()


def get_stats():
    raise NotImplementedError
