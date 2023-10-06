# this is a solution to the two sum problem on leetcode.com


class Solution:
    def twoSum(self, nums, target):
        # create a dictionary to store the values of the array
        # as keys and the indices as values
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i

        # loop through the array
        for i in range(len(nums)):
            # check if the complement of the current number is in the dictionary
            complement = target - nums[i]
            if complement in num_dict:
                # check if the complement is not the current number
                if num_dict[complement] != i: # this is to prevent using the same number twice
                    # return the indices of the two numbers
                    return [i, num_dict[complement]]
                
        # if no solution is found, return an empty array
        return []
    
    def twoSum2(self, nums, target):
        # create a dictionary to store the values of the array
        # as keys and the indices as values
        num_dict = {}
        for i in range(len(nums)):
            # check if the complement of the current number is in the dictionary
            complement = target - nums[i]
            if complement in num_dict:
                # check if the complement is not the current number
                if num_dict[complement] != i:
                    # return the indices of the two numbers
                    return [i, num_dict[complement]]
            # add the current number to the dictionary
            num_dict[nums[i]] = i
                
        # if no solution is found, return an empty array
        return []
    

if __name__ == '__main__':
    # create an instance of the Solution class
    sol = Solution()

    # create a list of numbers
    nums = [2, 7, 11, 15]
    # create a target number
    target = 9

    # call the twoSum function
    result = sol.twoSum(nums, target)
    print(result)

    # call the twoSum2 function
    result = sol.twoSum2(nums, target)
    print(result)
