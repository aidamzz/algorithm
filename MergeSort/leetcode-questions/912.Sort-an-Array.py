class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(left,right):
            i = 0
            j = 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i +=1
                else:
                    result.append(right[j])
                    j+= 1
            while( i < len(left)):
                    result.append(left[i])
                    i +=1
            while( j < len(right)):
                    result.append(right[j])
                    j +=1
            return result
        def divide(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left =divide(arr[:mid])
            right = divide(arr[mid:])
            return merge(left, right)
        return divide(nums)