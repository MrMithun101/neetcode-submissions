class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq_buckets = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for num, freq in count.items():
            freq_buckets[freq].append(num)

        result = []

        for i in range(len(freq_buckets)-1, 0, -1):
            result.extend(freq_buckets[i])

            if len(result) >= k:
                return result