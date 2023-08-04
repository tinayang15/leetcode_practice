# variables are dynamicly typed
import math
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

# while loops are similar to if

n = 0
while n < 5:
    print(n)
    n += 1

# looping from i = 0 to i = 4
# starts at 0 until it reaches 5
# i is incremented already by default
for i in range(5):
    print(i)

# looping from i = 2 to i = 6
for i in range(2, 6):
    print(i)

# looping from i = 5 to i = 2, decrementing -1
for i in range(5, 1, -1):
    print(i)

# for(int i = 0; i <n; i++)


# division is decimal by default
print(5/2)
# double slash rounds down
print(5//2)
# CAREFUL: most langs round towards 0 by default so negative numbers will round down
print(-3//2)
# workaround for rounding towards zero is to use decimal division and then cover to int
print(int(-3/2))

# modding is similar to most langs
print(10 % 3)  # solution is 1

# except for neg values
print(-10 % 3)  # solution is 2, needs to be negative number
# work around is below
print(math.fmod(-10, 3))  # solution is -1 = correct


# More math helpers
print(math.floor(3/2))  # round down
print(math.ceil(3/2))  # round up
print(math.sqrt(2))
print(math.pow(2, 3))  # first number to the power of second number


# max/min int
float("inf")  # max
float("-inf")  # min

# python numbers are infinite so they never overflow
print(math.pow(2, 200))

# but still less than infinity
print(math.pow(2, 200) < float("inf"))


# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)

# can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)  # at index 1, insert 7 O(n) time
print(arr)

# not O(n) to index array - reassign value
arr[0] = 0
arr[3] = 0
print(arr)


# intialize arr of size n with default value of 1
n = 5
arr = [1] * n
print("array", arr)
print("length", len(arr))


# careful: -1 is not out of bounds, it's the last value
arr = [1, 2, 3]
print(arr[-1])
# indexing -2 is the second to last value, etc
print(arr[-2])
