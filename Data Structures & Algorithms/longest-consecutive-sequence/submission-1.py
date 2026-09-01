class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        longest = 1
        starters = []
        for num in nums:
            if num - 1 in numSet:
                continue
            else:
                starters.append(num)

        for num in starters:
            current = 1
            while True:
                if num + 1 in numSet:
                    current += 1
                    num += 1
                else:
                    break

            longest = max(longest,current)

        return longest
