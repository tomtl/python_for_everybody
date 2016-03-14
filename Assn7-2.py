file_name = raw_input("Enter the file name:")
input_file = open(file_name)

count = 0
cumulative_total = 0
for line in input_file:
    if "X-DSPAM-Confidence:" in line:
        count += 1
        confidence_value = line[line.find(":") + 1 :].strip()
        cumulative_total += float(confidence_value)

average_confidence = cumulative_total / count
print "Average spam confidence:", average_confidence