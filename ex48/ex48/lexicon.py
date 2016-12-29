from lists import cats

def scan(line):
    # when given one or more directions (north, south, east west) return
    # a tuple ('direction', 'direc') for each direction
    line = line.split(' ')

    # look up each word in dictionary (cats) and return category
    # store as tuples in out_array
    out_array = list()
    for word in line:
        # Test if number and convert if so
        if word.isdigit():
            word = int(word)
            cat = 'number'
        # Retreive category if available
        elif cats.has_key(word.lower()):
            cat = cats[word.lower()]
        else:
            cat = "error"
        out_array.append((cat, word))
    return out_array
