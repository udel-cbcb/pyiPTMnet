from distutils.core import setup
setup(
  name = 'pyiptmnet',
  packages = ['pyiptmnet'], # this must be the same as the name above
  version = '0.1',
  description = 'Python client for iPTMNet REST API - https://research.bioinformatics.udel.edu/iptmnet/',
  author = 'Sachn Gavali',
  author_email = 'saching@udel.edu',
  url = 'https://github.com/udel-cbcb/pyiptmnet', # use the URL to the github repo
  download_url = 'https://github.com/udel-cbcb/pyiptmnet/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['iPTMnet', 'API', 'Client', 'REST-API'], # arbitrary keywords
  classifiers = [],
)