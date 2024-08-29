import csv

def process_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    file_path = 'testCsv.csv'
    process_csv(file_path)