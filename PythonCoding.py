# variables are dynamicly typed
n = 0
print('n=', n)

# n can be reassigned because no type assigned, type assigned at runtime
n = 'abc'
print('n =', n)

# multiple Assignments
n, m = 0, "abc"
print('n =', n, 'm =', m)

# increment
n = n+1  # good
n += 1  # good
# n++ #bad
# print('n =', n)
