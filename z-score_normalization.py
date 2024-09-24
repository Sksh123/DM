import csv
import math

# Function to calculate mean and standard deviation
def calculate_mean_and_std(values):
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    return mean, std_dev

# Function to perform Z-score normalization
def z_score_normalize(value, mean, std_dev):
    return (value - mean) / std_dev

# Read the CSV data
input_filename = 'normalized_data.csv'
output_filename = 'z_score_normalized_data.csv'

data = []
marks = []

# Read data and collect total marks
with open(input_filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip header
    data.append(header)  # Add header to data
    
    for row in reader:
        roll_no = row[0]
        total_marks = float(row[1])
        data.append([roll_no, total_marks])
        marks.append(total_marks)

# Calculate mean and standard deviation
mean, std_dev = calculate_mean_and_std(marks)

# Normalize the data using Z-score
normalized_data = [data[0]]  # Add header to normalized data
for row in data[1:]:
    roll_no = row[0]
    total_marks = row[1]
    normalized_marks = z_score_normalize(total_marks, mean, std_dev)
    normalized_data.append([roll_no, normalized_marks])

# Save normalized data to new CSV
with open(output_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(normalized_data)

print("Z-score normalization complete. The normalized data is saved in 'z_score_normalized_data.csv'.")
