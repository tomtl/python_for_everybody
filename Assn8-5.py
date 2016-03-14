filename = raw_input("Enter filename:") or "mbox-short.txt"
input_file = open(filename)

sender_count = 0
for line in input_file:
    if "From " in line:
        sender_count += 1
        words = line.split()
        print words[1]

print "There were %s lines in the file with From as the first word" % sender_count
