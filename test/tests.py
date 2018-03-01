import unittest
import iptmnet.api as api
import iptmnet.models as models
import jsonschema


def validate_items(items,schema):
    for index, item in enumerate(items):
        try:
            jsonschema.validate(item,schema)
        except jsonschema.exceptions.ValidationError as ve:
            raise jsonschema.exceptions.ValidationError("Record #{}: {}".format(index, str(ve)))


class IPTMnetTest(unittest.TestCase):
    maxDiff = None

    # setup
    def setUp(self):
        super().setUp()
        api.set_host_url("http://127.0.0.1:8080")

    # test search
    def test_search(self):
        search_results_df = api.search("smad2",models.Termtype.ProteinGeneName,models.Role.EnzymeOrSubstrate)
        self.assertTrue(len(search_results_df.index) != 0)

        search_results_dict = api.search("smad2", models.Termtype.ProteinGeneName, models.Role.EnzymeOrSubstrate,dict=True)
        validate_items(search_results_dict,models.SearchResult.schema)

    # test get info
    def test_get_info(self):
        info = api.get_info("Q15796")
        self.assertIsNotNone(info)
        jsonschema.validate(info, models.Info.schema)

    # test get proteoforms
    def test_get_substrates(self):
        proteoforms_df = api.get_substrates("Q15796")
        self.assertTrue(len(proteoforms_df.index) != 0)

    # test get proteoforms
    def test_get_proteoforms(self):
        proteoforms_df = api.get_proteoforms("Q15796")
        self.assertTrue(len(proteoforms_df.index) != 0)

        proteoforms_dict = api.get_proteoforms("Q15796",dict=True)
        validate_items(proteoforms_dict,models.Proteoform.schema)

    # test get ptm ppi
    def test_get_ptm_ppi(self):
        ptm_ppi_df = api.get_ptm_dependent_ppi("Q15796")
        self.assertTrue(len(ptm_ppi_df.index) != 0)

        ptm_ppi_dict = api.get_ptm_dependent_ppi("Q15796",dict=True)
        validate_items(ptm_ppi_dict,models.PTMPPI.schema)

    # test get ppi for proteoforms
    def test_get_ppi_for_proteoforms(self):
        ptm_ppi_df = api.get_ppi_for_proteoforms("Q15796")
        self.assertTrue(len(ptm_ppi_df.index) != 0)

        ptm_ppi = api.get_ppi_for_proteoforms("Q15796",dict=True)
        validate_items(ptm_ppi,models.ProteoformPPI.schema)

    # test get ptm enzymes from list
    def test_get_ptm_enzymes_from_list(self):
        substrates = [{
            "substrate_ac":"Q15796",
            "site_residue":"K",
            "site_position":"19"
        },
            {
                "substrate_ac": "Q15796",
                "site_residue": "T",
                "site_position": "8"
            },
            {
                "substrate_ac": "P04637",
                "site_residue": "K",
                "site_position": "120"
            },
        ]

        enzymes = api.get_ptm_enzymes_from_list(substrates)
        self.assertTrue(len(enzymes) != 0)
        validate_items(enzymes,models.BatchPTMEnzyme.schema)

    # test get ptm enzymes from file
    def test_get_ptm_enzymes_from_file(self):
        enzymes = api.get_ptm_enzymes_from_file("egfr_sites_formatted.txt")
        self.assertTrue(len(enzymes) != 0)
        validate_items(enzymes,models.BatchPTMEnzyme.schema)

    # test get ptm enzymes from list
    def test_get_ptm_ppi_from_list(self):
        substrates = [{
            "substrate_ac":"Q15796",
            "site_residue":"K",
            "site_position":"19"
        },
            {
                "substrate_ac": "Q15796",
                "site_residue": "T",
                "site_position": "8"
            },
            {
                "substrate_ac": "P04637",
                "site_residue": "K",
                "site_position": "120"
            },
            {
                "substrate_ac": "P04637",
                "site_residue": "S",
                "site_position": "149"
            },
            {
                "substrate_ac": "P04637",
                "site_residue": "S",
                "site_position": "378"
            },
        ]

        enzymes = api.get_ptm_ppi_from_list(substrates)
        self.assertTrue(len(enzymes) != 0)
        validate_items(enzymes,models.BatchPTMPPI.schema)

    # test get ptm enzymes from file
    def test_get_ptm_ppi_from_file(self):
        enzymes = api.get_ptm_ppi_from_file("egfr_sites_formatted.txt")
        self.assertTrue(len(enzymes) != 0)
        validate_items(enzymes,models.BatchPTMPPI.schema)