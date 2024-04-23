#=====================================
# Class Name: file_replicator_daemon.py
# Used For: Daemon running in background constantly replicating file(s)
#           in specific intervals.
# Version: 0.0.1
# Created By: Abhisek Ashirbad Sethy 
# Date: 18/03/2024 (18th Mar 2024)
#======================================

import time
import threading
from file_replicator.src.file_replicator import FileReplicator 

def replicate_files_daemon():
    print("File Replicator daemon is running...")

    while True:
        try:
            replicator = FileReplicator()
            replicator.replicate_files()
            print("File Replicator completed successfully.")
        except Exception as e:
            print(f"Error in replicating files: {e}")

        print("Waiting for next iteration of File Replicator.")
        print("File Replicator will run automatically in another 3 mins...")
        time.sleep(15*60)  # Wait for 15*60 seconds(15 minutes) before the next iteration

def main():
    try:
        thread = threading.Thread(target=replicate_files_daemon)
        thread.start()
        thread.join()  # Wait for the thread to complete
    except KeyboardInterrupt:
        print("File Replicator daemon stopped...")

if __name__ == "__main__":
    main()
