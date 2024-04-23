#=====================================
# Class Name: file_replicator_daemon.py
# Used For: Daemon running in background constantly deleting file(s)
#           which are older than specified intervals.
# Version: 0.0.1
# Created By: Abhisek Ashirbad Sethy 
# Date: 18/03/2024 (18th Mar 2024)
#======================================

import os
import shutil
import time
import threading

class CleanupDaemon:
    def __init__(self, config_file='application.properties'):
        self.config_file = config_file
        self.target_dir = self.get_target_dir()

    def get_target_dir(self):
        config = {}
        with open(self.config_file, 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                config[key.strip()] = value.strip()
        return config.get('target_dir', '')

    def cleanup_old_files(self):
        print("Cleanup Daemon is running...")

        while True:
            try:
                current_time = time.time()
                # Calculate the timestamp for 2 hours ago
                two_hours_ago = current_time - (2*60*60)

                # Iterate over files in the target directory
                for file_name in os.listdir(self.target_dir):
                    file_path = os.path.join(self.target_dir, file_name)
                    # Get the modification time of the file
                    modification_time = os.path.getmtime(file_path)
                    # If the file is older than 2 hours, delete it
                    if modification_time < two_hours_ago:
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                            print(f"Deleted old file: {file_name}")
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                            print(f"Deleted old directory: {file_name}")
            except Exception as e:
                print(f"Error in cleanup daemon: {e}")


def main():
    try:
        daemon = CleanupDaemon()
        thread = threading.Thread(target=daemon.cleanup_old_files)
        thread.start()
        thread.join()  # Wait for the thread to complete
    except KeyboardInterrupt:
        print("Cleanup Daemon stopped...")

if __name__ == "__main__":
    main()
