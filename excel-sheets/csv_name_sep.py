from csv import reader, writer

"""
IMPORTANT NOTES:

This file does NOT touch the title at all. Include the title row in the csv when porting into here

This file assumes the following format for names:
'FULL LAST NAME, FIRSTNAME'

This file assumes the full name is always contained in the first column

This file assumes everyone has a first name as well
"""

CSV_FILE_NAME = "names.csv"

if __name__ == "__main__":
    # Read lines from csv file
    lines = None
    with open(CSV_FILE_NAME, "r") as f:
        csv_read = reader(f, delimiter=",", quotechar='"')
        lines = list(csv_read)
    # Format the names of the students
    for i, row in enumerate(lines[1:]):
        name_entry = row[0]
        # Split by name
        last, first = [x.strip() for x in name_entry.strip().split(',')]
        # Modify output
        lines[i+1][0] = f'{first} {last}'
    # Write lines back to csv file
    with open(CSV_FILE_NAME, "w") as f:
        w = writer(f, delimiter=",", quotechar='"')
        w.writerows(lines)
