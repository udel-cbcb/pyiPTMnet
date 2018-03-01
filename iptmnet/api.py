import json
import requests
import csv
from io import StringIO
import pandas
__host_url = "https://annotation.dbi.udel.edu/iptmnet/api"

def set_host_url(url):
    global __host_url
    __host_url = url


def _to_dataframe(text):
    data = StringIO(text)
    dataframe = pandas.read_csv(data, sep=",")
    return dataframe


def search(search_term, term_type, role, ptm_list=None, organism_list=None, dict=None):
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

    url = "{host}/search".format(host=__host_url)

    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url,params=data,verify=False,headers=headers)

    if result.status_code is 200:
        # read the result
        if dict is True:
            search_results = json.loads(result.text)
        else:
            search_results = _to_dataframe(result.text)
        return search_results
    else:
        # raise the error
        result.raise_for_status()


def get_info(id,dict=None):
    url = "{host}/{id}/info".format(host=__host_url,id=id)
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


def get_substrates(id,dict=None):
    url = "{host}/{id}/substrate".format(host=__host_url,id=id)

    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url,verify=False,headers=headers)

    if result.status_code is 200:
        # read the result
        if dict is True:
            data = json.loads(result.text)
        else:
            data = _to_dataframe(result.text)
        return data
    else:
        # raise the error
        result.raise_for_status()


def get_proteoforms(id,dict=None):
    url = "{host}/{id}/proteoforms".format(host=__host_url,id=id)

    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url,verify=False,headers=headers)

    if result.status_code is 200:
        # read the result
        if dict is True:
            data = json.loads(result.text)
        else:
            data = _to_dataframe(result.text)
        return data
    else:
        # raise the error
        result.raise_for_status()


def get_ptm_dependent_ppi(id,dict=None):
    url = "{host}/{id}/ptmppi".format(host=__host_url,id=id)
    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url,verify=False,headers=headers)

    if result.status_code is 200:
        # read the result
        if dict is True:
            data = json.loads(result.text)
        else:
            data = _to_dataframe(result.text)
        return data
    else:
        # raise the error
        result.raise_for_status()

def get_ppi_for_proteoforms(id,dict=None):
    url = "{host}/{id}/proteoformppi".format(host=__host_url,id=id)
    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url,verify=False,headers=headers)

    if result.status_code is 200:
        # read the result
        if dict is True:
            data = json.loads(result.text)
        else:
            data = _to_dataframe(result.text)
        return data
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
    url = "{host}/batch_ptm_enzymes".format(host=__host_url)
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
    url = "{host}/batch_ptm_ppi".format(host=__host_url)
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


