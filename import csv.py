import csv

# Open the CSV file
with open('bestellungen.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Initialize a count of the number of rows that contain "Duschgel"
    duschgel_count = 0
    # Initialize a count of the total number of rows
    total_count = 0
    # Initialize a count of the total amount of Duschgel
    duschgel_amount = 0
    # Iterate over the rows in the CSV file
    for row in reader:
        total_count += int(row[6])
        if row[3] == 'Duschgel':
            duschgel_count += int(row[6])
            duschgel_amount += int(row[6])
    # Calculate the percentage of rows that contain "Duschgel"
    duschgel_percent = (duschgel_amount / total_count) * 100
    print(f'Duschgel makes up {duschgel_percent:.2f}% of the total amount of items.')
