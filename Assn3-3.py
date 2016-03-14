score = raw_input("Enter score:")
try :
    score = float(score)
except :
    print "Error: please enter a number."

if score < 0 :
    print "Error: Score must be between 0 and 1."
elif score < 0.6 :
    print "F"
elif score < 0.7 :
    print "D"
elif score < 0.8 :
    print "C"
elif score < 0.9 :
    print "B"
elif score <= 1.0 :
    print "A"
else :
    print "Error: Score must be between 0 and 1."