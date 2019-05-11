def routes_gen(file):
  """Takes the carrier list file and returns a list of tuples: (prefix, cost)"""
  with open(file) as routes:
    for route in routes:
        prefix, cost = route[:-1].split(',')
        yield (prefix, float(cost)) # returns a bunch of values without loading the whole thing into memory

def numbers_gen(file):
  with open(file) as numbers:
    for number in numbers:
      yield number[:-1]
