# setup/install file

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description'       :   'My Project',
    'author'            :   'Paul Rafferty',
    'url'               :   'github.com/mrraffo/mapgen',
    'download_url'      :   'github.com/mrraffo/mapgen',
    'author_email'      :   'paul_raffo@hotmail.com',
    'version'           :   '0.1',
    'install_requires'  :   ['nose', 'pygame'],
    'packages'          :   ['mapgen'],
    'scripts'           :   [],
    'name'              :   'Mapgen'
}

setup(**config)
