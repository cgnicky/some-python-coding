class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution explanation: https://www.youtube.com/watch?v=uCst0TJHJvg
                
        # Find the pivot point by comparing two items from the end
        i = len(nums) - 2
        
        # Keep finding the element where right greater than left
        while i >= 0 and nums[i] >= nums[i+1]: 
            i -= 1 # Moving left
        
        # If list is in descending order, just reserve it in ascending order to get the smallest combination
        if i < 0:
            l, r = 0, len(nums)-1
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        else:
            # Search the item from the end of list
            j = len(nums)  - 1
            
            # Find the first element that greater than pivot value
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1 # Moving left
            
            # swapping the position
            nums[i], nums[j] = nums[j], nums[i]
            
            # Sort the elements after the pivot position in ascending order
            nums[i+1:] = sorted(nums[i+1:])
            
