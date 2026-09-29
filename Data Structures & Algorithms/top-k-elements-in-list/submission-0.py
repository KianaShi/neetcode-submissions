class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(sorted_dic[i][0])
        return result