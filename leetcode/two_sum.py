# this is a solution to the two sum problem on leetcode.com
"""
author: Levi

title: Two Sum

problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

:Easy
"""



from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
                if (
                    num_dict[complement] != i
                    ):  # this is to prevent using the same number twice
                        # return the indices of the two numbers
                    return [i, num_dict[complement]]

            # if no solution is found, return an empty array
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                    # check if the sum of the two numbers is equal to the target
                if nums[i] + nums[j] == target:
                        # return the indices of the two numbers
                    return [i, j]
                    # if all number combinations are checked and no solution is found, return an empty array
        return []

if __name__ == "__main__":
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
