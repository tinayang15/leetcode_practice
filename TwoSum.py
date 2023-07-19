class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[n], i]
            prevMap[n] = i
        return

# nums=[integers]
# target is integer
# return [i] 2 integers from nums = target
# Each input has exactly 1 solution
# can't use same element twice

# class called solution


class Solution:
    # method which takes in the paramates self(instance of the class), nums which a list of integers, target which is an interger and returns a list of integers
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # empty dictionary which will store the nums values and indices
        prevMap = {}  # val:index
    # for loop that iterates over the elements in the nums list
    #  it'll return a tuple of index i and the element n at that index in each iteration
    # tuple contains 2 values: index and the value/item itself
        for i, n in enumerate(nums):
            # calculates the difference between target "value" and the current element "n" in the loop
            diff = target - n
            # checks if diff is present in the prevMap dictionary/hasmap.
            if diff in prevMap:
                # if yes - it will return the current index and the diff value's index that is found in the prevMap/hashmap
                return [prevMap[diff], i]
            prevMap[n] = i
        return
        # if not it just returns
