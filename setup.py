from distutils.core import setup
setup(
  name = 'pyiptmnet',
  packages = ['pyiptmnet'], # this must be the same as the name above
  version = '0.1.2',
  description = 'Python client for iPTMNet REST API - https://research.bioinformatics.udel.edu/iptmnet/',
  long_description = "PTMnet is a bioinformatics resource for integrated understanding of protein post-translational "
                     "modifications (PTMs) in systems biology context. "
                     "It connects multiple disparate bioinformatics tools and systems of text mining, data mining, "
                     "analysis and visualization tools, and databases and ontologies into an integrated cross-cutting "
                     "research resource to address the knowledge gaps in exploring and discovering PTM networks.",
  author = 'Sachn Gavali',
  author_email = 'saching@udel.edu',
  url = 'https://github.com/udel-cbcb/pyiptmnet', # use the URL to the github repo
  download_url = 'https://github.com/udel-cbcb/pyiptmnet/archive/0.1.2.tar.gz', # I'll explain this in a second
  keywords = ['iPTMnet', 'API', 'Client', 'REST-API'], # arbitrary keywords
  classifiers = [],
)