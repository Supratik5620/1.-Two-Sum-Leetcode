class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Iterate over each element in the 'nums' list, excluding the last element
        for i in range(len(nums) - 1):
            # Iterate over the elements following the current element 'i'
            # This ensures we don't repeat pairs we've already checked
            for j in range(i + 1, len(nums)):
                # Check if the sum of the current pair equals the target
                if nums[i] + nums[j] == target:
                    # Return the indices of the pair that sum up to the target
                    return [i, j]
        
        # If no pair is found, return None
        return None
