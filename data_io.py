import csv

def read_csv(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)
