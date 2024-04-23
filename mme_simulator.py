#=====================================
# Class Name: file_replicator_daemon.py
# Used For: Daemon running in background simulating the MME/AMF nodes
# Version: 0.0.1
# Created By: Abhisek Ashirbad Sethy 
# Date: 18/03/2024 (18th Mar 2024)
#======================================

import multiprocessing
import time
import file_replicator_daemon
import file_deletion_daemon

def start_daemons():
    # Create daemon processes
    file_replicator_process = multiprocessing.Process(target=file_replicator_daemon.main)
    file_deletion_process = multiprocessing.Process(target=file_deletion_daemon.main)

    # Start daemon processes
    file_replicator_process.daemon = True
    file_deletion_process.daemon = True
    file_replicator_process.start()
    time.sleep(60)
    file_deletion_process.start()

    # Keep the main process running indefinitely
    while True:
        time.sleep(1)

    '''
    replicator_thread = threading.Thread(target=file_replicator_daemon.main)
    replicator_thread.start()
    replicator_thread.join()  # Wait for file_replicator_daemon to complete
    '''
    # Wait for 5 minutes before starting the cleanup daemon
    # print("Waiting for 5 minutes before starting Cleanup Daemon...")
    # time.sleep(30)
    '''
    cleanup_thread = threading.Thread(target=file_deletion_daemon.main)
    cleanup_thread.start()
    cleanup_thread.join()  # Wait for file_cleanup_daemon to complete
    '''
if __name__ == "__main__":
    start_daemons()
