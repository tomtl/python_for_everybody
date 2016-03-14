largest = None
smallest = None

while True:
    user_input = raw_input("Enter an integer. Type 'done' to exit.")
    if user_input == "done":
        break

    try:
        num = int(user_input)
    except:
        print "Invalid input"
        continue

    if largest is None:
        largest = num

    if smallest is None:
        smallest = num

    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print "Maximum is", largest
print "Minimum is", smallest
