class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap (arr,first,last):
            temp = arr[first]
            arr[first] = arr[last]
            arr[last] = temp;

        def CyclicSort (arr):
            i = 0
            while ( i < len(arr) ):
                
                correct = arr[i] - 1
                
                if (arr[i] <= len(arr) and arr[i] > 0  and arr[i] != arr[correct]):
                    swap(arr,i,correct)
                else:
                    i += 1

            for j in range(0,len(arr)):

                if (arr[j] != j + 1):
                    return j + 1
            else:
                return len(arr) + 1

        return CyclicSort(nums)
