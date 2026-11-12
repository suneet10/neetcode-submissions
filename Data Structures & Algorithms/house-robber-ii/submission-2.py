class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def help(arr):
            if len(arr) == 1:

                return arr[0]

            x = max(arr[0],arr[1])
            y = arr[0]

            for i in range(2,len(arr)):

                temp = x
                x = max(x,y+arr[i])
                y = temp

            return x

        return max(help(nums[:-1]),help(nums[1:]))