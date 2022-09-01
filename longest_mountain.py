class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        
        downwardSlope = False
        length = 1
        max_length = 0
        
        for i in range(1, len(arr)):
            # If current value greater than previous value, climbing up
            if arr[i - 1] < arr[i]:
                if downwardSlope:
                    max_length = max(max_length, length)
                    length = 2
                    downwardSlope = False
                else:
                    length += 1
            # If current value is lesser than previous value, climbing down
            elif arr[i - 1] > arr[i]:
                # Set the downwardSlope to True if the previous climbing up length is greater than 2
                if length >= 2:
                    downwardSlope = True
                
                # Keep adding to length while climbing down
                if downwardSlope:
                    length += 1
                    
                    # Assign the longest length to max_length
                    max_length = max(max_length, length)
                else:
                    length = 1
            # Walking flat and reset the length to starting value
            else:
                length = 1
        
        return max_length
