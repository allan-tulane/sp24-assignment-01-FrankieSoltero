"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x ==0:
      return 0
    else:
      return x + foo(x-1)
    pass

def longest_run(mylist, key):
  seqAmnt = 0
  maxSeq = 0
  for number in mylist:
    if number == key and seqAmnt == 0:
      seqAmnt = 1
    elif number == key and seqAmnt > 0:
      seqAmnt += 1
    else:
      seqAmnt = 0
    if seqAmnt > maxSeq:
      maxSeq = seqAmnt
  return maxSeq
      


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    def find_longest_run(mylist, key, currentStreak, maxStreak):
      if not mylist:
        return maxStreak
      if mylist[0] == key:
        currentStreak += 1
        maxStreak = max(maxStreak, currentStreak)
      else:
        currentStreak = 0
      return find_longest_run(mylist[1:], key, currentStreak, maxStreak)
    return find_longest_run(mylist, key, 0, 0)
    pass



