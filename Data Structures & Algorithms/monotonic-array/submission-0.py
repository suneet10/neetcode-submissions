class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums) <= 2:
            return True

        flag = "not_set"
        order = "unknown"

        for j in range(1,len(nums)):
            i = j-1
            if nums[i] == nums[j]:
                continue
            else:
                if nums[i] < nums[j]:
                    if flag == "not_set":
                        flag = "is_set"
                        order = "dec"
                    else:
                        if order != "dec":
                            return False

                elif nums[i] > nums[j]:
                    if flag == "not_set":
                        flag = "is_set"
                        order = "inc"
                    else:
                        if order != "inc":
                            return False

        return True