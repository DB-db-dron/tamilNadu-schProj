import csv
import pickle

csv_file_path = 'temples.csv'
pickle_file_path = 'temple_data.dat'

data = []

# Read data from CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append({
            "code": row[0],
            "name": row[1].lower(),
            "city": row[2].lower(),
            "deity": row[3].lower(),
            "dynasty": row[4].lower(),
            "century": row[5].lower(),
            "remark": row[6].lower()
        })

# Store data in pickle file
with open(pickle_file_path, 'wb') as file:
    pickle.dump(data, file)
