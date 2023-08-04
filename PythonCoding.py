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


# None is null (absence of value)
n = 4
n = None
print("n =", n)


# if statements don't need parenthesis or curly braces
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# parenthesis needed for multi-line conditions.
# and = &&
# or = ||

n, m = 1, 2
if ((n > 2 and n != m) or n == m):
    n += 1
