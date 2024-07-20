import threading
import os

def process_file(file_path):
    with open(file_path, 'r') as f:
        # Process the file contents here
        for line in f:
            # Example: print each line
            print(line, end='')

def main():
    # Directory containing the files to process
    directory = '/path/to/directory'

    # Create a list of files to process
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Create a lock to ensure only one thread processes a file at a time
    file_lock = threading.Lock()

    # Create and start threads to process the files
    threads = []
    for file_path in files:
        thread = threading.Thread(target=process_file, args=(file_path,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()