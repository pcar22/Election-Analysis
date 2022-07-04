from importlib import resources

# add our dependencies.
import csv
import os
from wsgiref import headers

# Assign a variable to laod a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:


# To do: read and analyze the data here.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # for row in file_reader:
        # print(row)

    # Print the header row.
    headers = next(file_reader)
    print(headers)





