hours = float(raw_input("Enter hours:"))
rate = float(raw_input("Enter rate:"))

if hours <= 40 :
    pay = hours * rate
else :
    pay = (hours * rate) + ((hours - 40) * (rate * 0.5))

print pay