from sys import argv

script, filename = argv

tmp = open(filename)

print tmp.read()

tmp.close()
