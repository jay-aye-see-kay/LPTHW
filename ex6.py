# format 10 as a decimal
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# format these two variables as strings
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x # print this one as raw output (use for debugging)
print "I also said: '%s'." % y # print this one as a string (normal)

hilarious = False
# using that raw format again
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
