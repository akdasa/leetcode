class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        count = len(nums)
        leftSum, rightSum, result = [], [], []
        ls, rs = 0, 0

        for n in range(count):
            leftSum.append(ls)
            rightSum.insert(0, rs)
            ls += nums[n]
            rs += nums[count - n - 1]

        for n in range(count):
            result.append(abs(leftSum[n] - rightSum[n]))

        return result
