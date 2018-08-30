# 894. All Possible Full Binary Trees

'''
---Description---

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.
Each node of each tree in the answer must have node.val = 0.
You may return the final list of trees in any order.

Example 1:
Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Note:
1 <= N <= 20
'''

'''
---Thought---
The nodes number of a full binary tree must be odd.
When realizing this, the problem can be solved by recursion, since the sub-tree of a full binary tree must be a full tree too.
Use a length-fixed list to remember the temp results to save time.
The problem can also be solve by a loop, which is opposite to recursion.
The calculation of time & space complexity is quite :).
'''

'''
---My solution---
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        record = [None] * (20 + 1)
        record[1] = [TreeNode(0)]
        def recursion(n):
            if record[n]:
                return record[n]
            tmp = []
            for i in range(1, n, 2):
                left, right = recursion(i), recursion(n - 1 - i)
                for l in left:
                    for r in right:
                        tmp_node = TreeNode(0)
                        tmp_node.left = l
                        tmp_node.right = r
                        tmp.append(tmp_node)
            record[n] = tmp
            return tmp
        return recursion(N)
        

'''
---Official Solution---
Approach 1: Recursion

Intuition and Algorithm
Let \text{FBT}(N)FBT(N) be the list of all possible full binary trees with NN nodes.
Every full binary tree TT with 3 or more nodes, has 2 children at its root. Each of those children left and right are themselves full binary trees.
Thus, for N \geq 3N≥3, we can formulate the recursion: \text{FBT}(N) =FBT(N)= [All trees with left child from \text{FBT}(x)FBT(x) and right child from \text{FBT}(N-1-x)FBT(N−1−x), for all xx].
Also, by a simple counting argument, there are no full binary trees with a positive, even number of nodes.
Finally, we should cache previous results of the function \text{FBT}FBT so that we don't have to recalculate them in our recursion.

class Solution(object):
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []
            for x in xrange(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]

Complexity Analysis
Time Complexity: O(2^N)(For odd NN, let N = 2k + 1N=2k+1. Then, \Big| \text{FBT}(N) \Big| = C_k)
Space Complexity: O(2^N)
'''

'''
---Discuss Solution---
python concise solution without cache. It won't be theoretically better if we cache previous results
It won't be theoretically better if we cache previous results, because the time complexity and space complexity are always equal to the size of the output.

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        def constr(N):
            if N == 1:
                yield TreeNode(0)
            for i in range(1, N, 2):
                for x in constr(i):
                    for y in constr(N - i - 1):
                        u = TreeNode(0)
                        u.left = x
                        u.right = y
                        yield u
        return list(constr(N))
'''
