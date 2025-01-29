class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X=0
        for i in operations:
            if i in ['X++','++X']:
                X=X+1
            elif i in ['X--','--X']:
                X=X-1
        return X