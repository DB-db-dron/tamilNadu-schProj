import csv
import pickle

csv_file_path = 'temples.csv'
pickle_file_path = 'temple_data.pkl'

data = []

# Read data from CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

# Store data in pickle file
with open(pickle_file_path, 'wb') as file:
    pickle.dump(data, file)
