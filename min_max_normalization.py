import csv

# Function to perform min-max normalization
def min_max_normalize(value, min_val, max_val, new_min, new_max):
    return ((value - min_val) / (max_val - min_val)) * (new_max - new_min) + new_min

# Read the CSV data
input_filename = 'Student_Final_Result - Sheet1.csv'
output_filename = 'normalized_data.csv'

data = []
min_marks = float('inf')
max_marks = float('-inf')

# Read data and find min and max values
with open(input_filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip header
    data.append(header)  # Add header to data
    
    for row in reader:
        roll_no = row[0]
        total_marks = float(row[1])
        data.append([roll_no, total_marks])
        
        if total_marks < min_marks:
            min_marks = total_marks
        if total_marks > max_marks:
            max_marks = total_marks

# Define the new range for normalization
new_min = 0
new_max = 1

# Normalize the data
normalized_data = [data[0]]  # Add header to normalized data
for row in data[1:]:
    roll_no = row[0]
    total_marks = row[1]
    normalized_marks = min_max_normalize(total_marks, min_marks, max_marks, new_min, new_max)
    normalized_data.append([roll_no, normalized_marks])

# Save normalized data to new CSV
with open(output_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(normalized_data)

print("Normalization complete. The normalized data is saved in 'normalized_data.csv'.")
