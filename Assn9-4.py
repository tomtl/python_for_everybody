filename = raw_input("Enter filename:") or "mbox-short.txt"
input_file = open(filename)

sender_counts = {}
for line in input_file:
    if "From " in line:
        words = line.split()
        sender = words[1]
        sender_counts[sender] = sender_counts.get(sender, 0) + 1

maximum_sender_count = max(sender_counts.values())
for key,value in sender_counts.items():
    if value == maximum_sender_count:
        print key, value