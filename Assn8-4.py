filename = raw_input("Enter filename:") or "romeo.txt"
input_file = open(filename)

words_in_file = []
for line in input_file:
    words_in_line = line.split()

    for word in words_in_line:
        if word not in words_in_file:
            words_in_file.append(word)

words_in_file.sort()
print words_in_file