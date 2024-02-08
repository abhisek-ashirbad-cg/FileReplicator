#=====================================
# Class Name: CleanupScript
# Used For: Cleaning up all the generated files in the target_dir.
# Version: 0.0.2
# Created By: Abhisek Ashirbad Sethy 
# Date: 31/01/2024 (31st Jan 2024)
#======================================


# Import modules
import os
import shutil
from tqdm import tqdm

# Cleanup Script Class
class CleanupScript:
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

    def cleanup_output_directory(self):
        # Check if the target directory exists
        if not os.path.exists(self.target_dir):
            print(f"Output directory '{self.target_dir}' does not exist.")
            return

        # Check if the target directory is empty
        if not os.listdir(self.target_dir):
            print(f"Output directory '{self.target_dir}' is already empty.")
            return

        # Display a warning and prompt the user for confirmation
        print(f"WARNING: Cleaning up output directory '{self.target_dir}'. This will delete all files in the directory.")
        user_input = input("Are you sure you want to proceed? (yes/no): ").lower()

        if user_input in {'yes', 'y'}:
            # Perform the cleanup by deleting all files in the target directory
            files_to_remove = os.listdir(self.target_dir)
            progress_bar = tqdm(total=len(files_to_remove), desc="Cleaning up Files")

            for file_name in files_to_remove:
                file_path = os.path.join(self.target_dir, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    progress_bar.update(1)
                except Exception as e:
                    print(f"Error while deleting '{file_path}': {e}")

            progress_bar.close()
            print(f"\nCleanup completed. Output directory '{self.target_dir}' is now empty.")
        else:
            print("Cleanup canceled.")

if __name__ == "__main__":
    cleanup_script = CleanupScript()
    cleanup_script.cleanup_output_directory()
