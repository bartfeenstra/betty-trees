"""Integrates Trees for Betty with Python's setuptools."""
from glob import glob
from pathlib import Path

from setuptools import setup, find_packages

from betty_trees import ROOT_DIRECTORY_PATH

with open(ROOT_DIRECTORY_PATH / 'VERSION', encoding='utf-8') as f:
    VERSION = f.read()

with open(ROOT_DIRECTORY_PATH / 'README.md', encoding='utf-8') as f:
    long_description = f.read()

SETUP = {
    'name': 'betty_trees',
    'description': 'Trees for Betty',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'version': VERSION,
    'license': 'GPLv3',
    'author': 'Bart Feenstra & contributors',
    'author_email': 'bart@mynameisbart.com',
    'url': 'https://github.com/bartfeenstra/betty',
    'classifiers': [
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: JavaScript',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Sociology :: Genealogy',
    ],
    'python_requires': '~= 3.7',
    'install_requires': [
        'betty ~= 0.3.0',
    ],
    'extras_require': {
        'development': [
            'autopep8 ~= 1.6.0',
            'codecov ~= 2.1.12',
            'coverage ~= 6.3',
            'flake8 ~= 4.0.1',
            'nose2 ~= 0.10',
        ],
    },
    'entry_points': {
        'betty_trees.extensions': [
            'betty_trees.extension.trees.Trees=betty_trees.extension.trees.Trees',
        ],
    },
    'packages': find_packages(),
    'data_files': [
        ('', [
            'LICENSE.txt',
            'README.md',
            'VERSION',
        ])
    ],
    'include_package_data': True,
    'package_data': {
        'betty_trees': list(map(str, [
            data_path
            for data_path
            in [
                ROOT_DIRECTORY_PATH / 'VERSION',
                *map(Path, glob(str(ROOT_DIRECTORY_PATH / 'betty_nginx' / 'assets' / '**'), recursive=True)),
            ]
            if data_path.is_file()
        ]))
    },
}

if __name__ == '__main__':
    setup(**SETUP)
