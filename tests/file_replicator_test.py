#=====================================
# Class Name: FileReplicator
# Used For: Creating given replicas for files in the source_dir.
# Version: 0.0.1
# Created By: Abhisek Ashirbad Sethy 
# Date: 24/01/2024 (24th Jan 2024)
#======================================

# Import modules
import unittest
from file_replicator.src import FileReplicator
import os

class FileReplicatorTest(unittest.TestCase):

    """
    TestFileReplicator Module

    This module contains unit tests for the FileReplicator class.

    Example:
        python -m unittest tests/test_file_replicator.py

    Attributes:
        TestFileReplicator: A class containing unit tests for the FileReplicator class.

    """

    # Initialization of configuration file as `application_test.properties`
    def setUp(self):
        self.replicator = FileReplicator(config_file='application.properties')

    # Extracting configuration settings from the initialised configuration file
    def test_load_config(self):
        self.assertEqual(self.replicator.config, {'src_dir': 'source', 'target_dir': 'destination', 'replicas': '2'})

    # Method for replicating files according to the configuration settings.
    def test_replicate_files(self):
        self.replicator.replicate_files()
        # Add assertions to check the correctness of replication, file counts, etc.

# Main method for testing
if __name__ == '__main__':
    unittest.main()
