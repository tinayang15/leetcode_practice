def hourglassSum(arr):
    # Write your code here
    maxsum = -99
    for i in range(4):
        for j in range(4):
            # top
            top = sum(arr[i][j:j+3])
            # mid
            mid = arr[i+1][j+1]
            # bottom
            bot = sum(arr[i+2][j:j+3])
            # total
            total = top + mid + bot
            maxsum = max(total, maxsum)
    return maxsum
