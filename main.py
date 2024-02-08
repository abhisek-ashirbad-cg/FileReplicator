#=====================================
# File Name: main.py
# Used For: Running the FileReplicator module
# Version: 0.0.1
# Created By: Abhisek Ashirbad Sethy 
# Date: 24/01/2024 (24th Jan 2024)
#======================================

# Import modules
from file_replicator.src.file_replicator import FileReplicator

# Main method
if __name__ == "__main__":
    replicator = FileReplicator()
    replicator.replicate_files()
