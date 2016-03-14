def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    elif hours > 40:
        pay = (hours * rate) + ((hours - 40) * (rate * 0.5))
    return pay

hours = float(raw_input("Enter hours:"))
rate = float(raw_input("Enter rate:"))

print computepay(hours, rate)