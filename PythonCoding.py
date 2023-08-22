# variables are dynamicly typed
import heapq
from collections import deque
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


new_arr = [1, 2, 3]

for i in range(0, len(new_arr)):
    print("here", i)


# sublists (aka slicing)
arr = [1, 2, 3, 4]
# prints index 1 - 3, but not including index 3
print(arr[1:3])

# similar to  for-loop ranges, last index is non-inclusive
print(arr[0:4])


# unpacking, make sure both sides matches
a, b, c, = [1, 2, 3]
print(a, b, c)

# loop through arrays
nums = [1, 2, 3]
# using index
for i in range(len(nums)):
    print("here", nums[i])

# without index
for n in nums:
    print(n)

# with index and value
for i, n in enumerate(nums):
    print(i, n)

# loop through multiple arrays simultaneously without unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
# zip takes both arrays and combine them into array of pairs and unpacks these values
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)


# reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)

# sorting array
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)  # sorts ascending

arr.sort(reverse=True)
print(arr)


# sort string
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)  # sorted alphabettically

# costum sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)
# function without a name - lambda, take every value of array and call it x and return the length of x - key to sort string - sorted in ascending order.


# list comprehension - intialize list
arr = [i for i in range(5)]  # taking i and adding it to the list - shorthand
print("dude", arr)

arr = [i+i for i in range(5)]  # taking i and adding it to the list - shorthand
print(arr)


# 2-D lists
arr = [[0]*4 for i in range(4)]
print(arr)


# strings are similar to arrays
s = 'abc'
print(s[0:2])

# So this creates a new string
s += "def"
print(s)


# valid numeric strings can be coverted
print(int("123")+int("123"))

# in rare cases you you may need the ASCII value of a char
print(ord("a"))
print(ord("b"))

# combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))


# queues (double ended queue)
queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)


# hash set
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))
# can't be double, can only have 1 unique
print(1 in mySet)
print(2 in mySet)

mySet.remove(2)
print(2 in mySet)


# list to set
print(set([1, 2, 3]))

# set comprehension
mySet = {i for i in range(5)}
print(mySet)


# hashmap aka dict
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 7
print(myMap)
print(len(myMap))
print(myMap.values())

myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap)

myMap.pop("alice")
print("alice" in myMap)

myMap = {"alice": 90, "bob": 70}
print(myMap)


# dict comprehension
myMap = {i: 2*i for i in range(3)}
print(myMap)

# looping through maps
myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key, myMap[key])

for value in myMap.values():
    print(value)

for key, value in myMap.items():
    print(key, value)


# tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

# can't modify
# tup[0] = 0

# can be used as key for hashmap/set
myMap = {(1, 2): 3}
print(myMap[(1, 2)])

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)


# lists can't be keys in hashmap
# myMap[[3,4]] = 5 #can't happen

# heaps

# under hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print("start", heapq.heappop(minHeap))

# no max heaps by default, work around is to use min heap and mulitply by -1 when push and pop

maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# max is awlays at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))


# functions
def myFunction(n, m):
    return n * m


print(myFunction(3, 4))


# nested functions
def outer(a, b):
    c = "c"

    def inner():
        return a+b+c
    return inner()


print(outer("a", "b"))

# can modify objects but can not reassign unless using nonlocal keyword


def double(arr, val):
    def helper():
        # modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        # will only modify val in the helper scope
        # val *= 2
        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)


nums = [1, 2]
val = 3
double(nums, val)


# class
class MyClass:
    # Constructor
    def __init__(self, nums):
        # create member vari
        self.nums = nums
        self.size = len(nums)

    # self keyword required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2*self.getLength()
