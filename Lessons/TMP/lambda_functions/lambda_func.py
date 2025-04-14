friends = ['Mike', 'Alice', 'Bob']

hi1 = lambda lst: [print('hi', name) for name in lst]
# hi1(friends)

hi11 = lambda lst: print('hi', ', '.join(lst))

hi11(friends)

def hi2(lst): [print('2 hi', name) for name in lst]

# hi2(friends)