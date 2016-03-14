import re

filename = "regex_sum_238314.txt"
input_file = open(filename)

sum = 0
line_numbers = []
for line in input_file :
    line_numbers = re.findall('[0-9]+', line)
    if len(line_numbers) < 1 : continue
    for number_string in line_numbers :
        try :
            sum += int(number_string)
        except :
            continue

print sum
