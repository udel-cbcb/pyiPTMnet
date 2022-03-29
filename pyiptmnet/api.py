import json
import requests
import csv
from io import StringIO
import pandas
from pandas.io.json import json_normalize
import urllib3
from pyiptmnet.enums import API_VERSION

__host_url = "https://research.bioinformatics.udel.edu/iptmnet/api"
urllib3.disable_warnings()
__selected_version = None

def set_host_url(url):
    global __host_url
    __host_url = url

def set_api_version(version):
    global __selected_version
    __selected_version = version

def _to_dataframe(text):
    data = StringIO(text)
    dataframe = pandas.read_csv(data, sep=",")
    return dataframe

def _to_dataframe_from_json(json):
    dataframe = json_normalize(json)
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
        "search_term": search_term,
        "term_type": term_type.value,
        "ptm_type": ptm_list,
        "role": role.value,
        "organism": organism_list
    }

    base_url = __get_base_url()
    url = f"{base_url}/search"

    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url, params=data, verify=False, headers=headers)

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


def get_info(id, dict=None):
    base_url = __get_base_url()
    url = f"{base_url}/{id}/info"
    result = requests.get(url, verify=False)

    if result.status_code is 200:
        # read the result
        info = json.loads(result.text)
        return info
    else:
        # raise the error
        result.raise_for_status()


def get_msa(id,dict=None):
    base_url = __get_base_url()
    url = f"{base_url}/{id}/msa"
    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url, verify=False, headers=headers)

    if result.status_code is 200:
        # read the result
        if dict is True:
            data = json.loads(result.text)
        else:
            data = json.loads(result.text)
            return data
    else:
        # raise the error
        result.raise_for_status()


def get_substrates(id, dict=None):
    base_url = __get_base_url()
    url = f"{base_url}/{id}/substrate"

    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url, verify=False, headers=headers)

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


def get_proteoforms(id, dict=None):
    base_url = __get_base_url()
    url = f"{base_url}/{id}/proteoforms"

    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url, verify=False, headers=headers)

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


def get_ptm_dependent_ppi(id, dict=None):
    base_url = __get_base_url()
    url = f"{base_url}/{id}/ptmppi"

    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url, verify=False, headers=headers)

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


def get_ppi_for_proteoforms(id, dict=None):
    base_url = __get_base_url()
    url = f"{base_url}/{id}/proteoformsppi"
    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url, verify=False, headers=headers)

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


def get_ptm_enzymes_from_file(file_name,dict=None):
    sites = __get_sites_from_files(file_name)

    return __get_data(sites,get_ptm_enzymes_from_list,dict=dict)


def get_ptm_enzymes_from_list(items,dict=None):
    base_url = __get_base_url()
    url = f"{base_url}/batch_ptm_enzymes"
    json_data = json.dumps(items, indent=4)

    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.post(url, data=json_data, verify=False,headers=headers)

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


def get_ptm_ppi_from_file(file_name,dict=None):
    sites = __get_sites_from_files(file_name)
    return __get_data(sites,get_ptm_ppi_from_list,dict=dict)


def get_ptm_ppi_from_list(items,dict=None):
    base_url = __get_base_url()
    url = f"{base_url}/batch_ptm_ppi"
    json_data = json.dumps(items, indent=4)

    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.post(url, data=json_data, verify=False,headers=headers)

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

def get_variants(id, dict=None):
    base_url = __get_base_url()
    url = f"{base_url}/{id}/variants"

    if dict is True:
        headers = {"Accept": "application/json"}
    else:
        headers = {"Accept": "text/plain"}

    result = requests.get(url, verify=False, headers=headers)

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


def get_stats():
    raise NotImplementedError


def __get_sites_from_files(file_name):
    sites = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for substrate_ac, site_residue, site_position in reader:
            site = {
                "substrate_ac": substrate_ac,
                "site_residue": site_residue,
                "site_position": site_position
            }
            sites.append(site)
    return sites

def __get_data(sites, get_data_func,dict=None):
    data = None
    if len(sites) <= 1000:
        data = get_data_func(sites,dict=dict)
        return data
    else:
        # get the first 1000
        loops = len(sites) // 1000
        for index in range(0, loops):
            start_index = (index * 1000)
            end_index = start_index + 1000
            sub_sites = sites[start_index:end_index]
            if index == 0:
                data = get_data_func(sub_sites,dict=dict)
            else:
                new_data = get_data_func(sub_sites,dict=dict)
                if data is not None:
                    if dict is True:
                        data = data + new_data
                    else:
                        data = data.append(new_data)
                else:
                    data = new_data

        remainders = len(sites) % 1000
        if remainders != 0:
            start_index = (loops * 1000) + 1
            end_index = len(sites)
            new_data = get_data_func(sites[start_index:end_index],dict=dict)
            if data is not None:
                if dict is True:
                    data = data + new_data
                else:
                    data = data.append(new_data)
            else:
                data = new_data

        return data


def __get_base_url():
    if __selected_version == None:
        return __host_url
    else:
        return f"{__host_url}/{__selected_version}"

