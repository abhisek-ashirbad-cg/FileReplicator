#=====================================
# Class Name: FileReplicator
# Used For: Creating given replicas for files in the source_dir.
# Version: 0.0.1
# Created By: Abhisek Ashirbad Sethy 
# Date: 24/01/2024 (24th Jan 2024)
#======================================

# Import modules
import shutil
import os
from tqdm import tqdm

class FileReplicator:

    """
    FileReplicator Module

        This module contains the FileReplicator class, which reads a configuration file
    containing source and target directories and the number of replicas for each file.

    Example:
        replicator = FileReplicator()
        replicator.replicate_files()

    Attributes:
        FileReplicator: A class for replicating files based on a configuration file.

    """

    # Initialization of configuration file as `application.properties`
    def __init__(self, config_file='application.properties'):
        self.config = self.load_config(config_file)

    # Extracting configuration settings from the initialised configuration file
    def load_config(self, config_file):
        config = {}
        with open(config_file, 'r') as f:
            for line in f:
                print(line)
                key, value = line.strip().split('=')
                config[key.strip()] = value.strip()
        return config

    # Validate the directories mentioned in the configuration file
    def validate_directories(self):
        src_dir = self.config.get('src_dir')
        target_dir = self.config.get('target_dir')

        if not os.path.exists(src_dir):
            raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")
        
        if not os.path.exists(target_dir):
            raise FileNotFoundError(f"Target directory '{target_dir}' does not exist.")


    # Method for replicating files according to the configuration settings.
    def replicate_files(self):
        self.validate_directories()

        src_dir = self.config.get('src_dir')
        target_dir = self.config.get('target_dir')
        replicas = int(self.config.get('replicas', 1))

        total_files = len(os.listdir(src_dir))
        progress_bar = tqdm(total=total_files * replicas, desc="Replicating Files")

        for filename in os.listdir(src_dir):
            src_path = os.path.join(src_dir, filename)
            file_name_parts = filename.split('.')
            
            # Extracting file name without extension
            base_name = ".".join(file_name_parts[:-1])
            ext_name = file_name_parts[-1]

            for replica_num in range(1, replicas + 1):
                replica_filename = f"{base_name}_copy_{replica_num}.{ext_name}"
                target_path = os.path.join(target_dir, replica_filename)
                shutil.copy(src_path, target_path)
                progress_bar.update(1)

        progress_bar.close()
  

# Main method
if __name__ == "__main__":
    try:
        replicator = FileReplicator()
        replicator.replicate_files()
    except Exception as e:
        print(f"Error: {e}")