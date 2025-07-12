'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def areMirror(self, a, b):
        '''
        :param root1,root2: two root of the given trees.
        :return: True False
        
        '''
        #code here
        if not a and not b:
            return True
        if not a or not b or a.data!=b.data:
            return False
        return self.areMirror(a.left,b.right) and self.areMirror(a.right,b.left)
