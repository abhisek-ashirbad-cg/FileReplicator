#=====================================
# File Name: setup.py
# Used For: Packaging the FileReplicator module for distribution
# Version: 0.0.1
# Created By: Abhisek Ashirbad Sethy 
# Date: 24/01/2024 (24th Jan 2024)
#======================================

from setuptools import setup, find_packages

setup(
    name='file_replicator',
    version='1.0.0',
    packages=find_packages(where='file_replicator/src'),
    install_requires=[
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'file_replicator=file_replicator.src.file_replicator:FileReplicator.replicate_files',
        ],
    },
    # Specify the output directory for distribution files
    script_args=['bdist_wheel', '--dist-dir', 'dist'],
)
