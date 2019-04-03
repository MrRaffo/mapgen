# setup/install file

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description'       :   'My Project',
    'author'            :   'Paul Rafferty',
    'url'               :   'URL to get it.',
    'download_url'      :   'Where to download it.',
    'author_email'      :   'paul_raffo@hotmail.com',
    'version'           :   '0.1',
    'install_requires'  :   ['nose'],
    'packages'          :   ['NAME'],
    'scripts'           :   [],
    'name'              :   'projectname'
}

setup(**config)
