import csv

def process_csv(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

# Usage
process_csv('testCsv.csv')