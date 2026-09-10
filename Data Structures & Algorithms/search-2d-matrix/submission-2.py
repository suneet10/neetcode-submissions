class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(arr,i,j,x):

            if i == j:
                if arr[i] == x:
                    return True
                else:
                    return False

            if x <= arr[(i+j)//2]:

                return binarySearch(arr,i,((i+j)//2),x)

            elif x > arr[(i+j)//2]:

                return binarySearch(arr,((i+j)//2)+1,j,x)
        
        def findRow():
            for i in matrix:
                
                if i[-1] >= target:
                    return i

            return False

        def findRow_bs(matrix,i,j,x):

            while i <= j:

                if i == j:

                    if  matrix[i][-1] >= target:
                        return matrix[i]
                    else:
                        return False
                    
                elif matrix[(i+j)//2][-1] >= target:
                    j = (i+j)//2

                else:
                    i = ((i+j)//2)+1

        arr = findRow_bs(matrix,0,(len(matrix))-1,target)

        if arr == False:
            return False

        return binarySearch(arr,0,(len(arr)-1),target)

        
        