from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'pyiptmnet',
  packages = ['pyiptmnet'], # this must be the same as the name above
  version = '0.1.7',
  description = 'Python client for iPTMNet REST API - https://research.bioinformatics.udel.edu/iptmnet/',
  long_description = long_description,
  long_description_content_type="text/markdown",
  author = 'Sachn Gavali',
  author_email = 'saching@udel.edu',
  url = 'https://github.com/udel-cbcb/pyiptmnet', # use the URL to the github repo
  download_url = 'https://github.com/udel-cbcb/pyiptmnet/archive/0.1.7.tar.gz',
  keywords = ['iPTMnet', 'API', 'Client', 'REST-API'], # arbitrary keywords
  classifiers = [],
  install_requires=[
   'certifi',
   'chardet',
   'idna',
   'jsonschema',
   'numpy',
   'pandas',
   'python-dateutil',
   'pytz',
   'requests',
   'six',
   'urllib3'
  ]
)