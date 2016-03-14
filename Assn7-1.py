file_name = raw_input("Enter the file name:")
input_file = open(file_name)

for line in input_file:
    print line.rstrip().upper()