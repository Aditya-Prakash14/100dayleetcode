class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        if not target:
            return 0
        opration = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                opration += target[i] - target[i - 1]
        return opration
 
        