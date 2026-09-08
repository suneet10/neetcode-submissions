class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bsearch(i,j,x):
            # print(i,j,x)

            if j - i == 0:
                if nums[i] != x:
                    return -1

                else:
                    return i

            if nums[(i+j)//2] >= x:
                # print(1)
                return bsearch(i,(i+j)//2,x)

            else:
                # print(2)
                return bsearch(((i+j)//2)+1,j,x)

        return bsearch(0,len(nums)-1,target)