from heapq import heappush, heappop

# variable is an object num = array
heap = []
lookup = set()

# take in 1 query and store it in num and then add 2 query and add it to num.
# 1 v = insert
for i in range(int(input())):
    t = list(map(int, input().split()))
    if t[0] == 1:
        heappush(heap, t[1])
        lookup.add(t[1])
# delete 4 from num
    # 2 v = delete
    elif t[0] == 2:
        lookup.discard(t[1])
# Use num and print minimum
    # 3 = print
    else:
        while heap[0] not in lookup:
            heappop(heap)
        print(heap[0])
# print minimum from num
    # 3 = print
