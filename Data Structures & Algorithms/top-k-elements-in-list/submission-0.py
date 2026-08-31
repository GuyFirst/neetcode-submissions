from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # buckets[i] contains numbers appearing i times
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in count.items():
            buckets[frequency].append(num)

        # Collect the k most frequent elements
        result = []

        for frequency in range(len(nums), 0, -1):
            for num in buckets[frequency]:
                result.append(num)

                if len(result) == k:
                    return result

        return result