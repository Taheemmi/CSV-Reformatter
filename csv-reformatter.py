import csv

with open('FILE_INPUT_HERE', 'r') as input_file: # Location of spreadsheet which needs reformating.
    reader = csv.reader(input_file)
    next(reader)  # Skip the header row

    with open('FILE_OUTPUT_HERE', 'w', newline='') as output_file: #Change the location and file name to your choice.
        writer = csv.writer(output_file)
        writer.writerow(["Number","month no", "Value"]) # Headers which will be displayed on output file, change to required and able to add more if required

        for row in reader:
            part_number = row[0] # Indicates the start, change to whatever is the first on your sheet.
            for i in range(1, 13):  # This will read 12 collumns for the value, change if more.
                writer.writerow([part_number, i, row[i]]) # Change part_number to whatever the varible in line 12 is.
