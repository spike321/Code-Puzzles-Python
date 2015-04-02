class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        sum = root
        temp = root
        while(temp.left):
            sum += temp.left
            temp = temp.left
        temp2 = root
        while(temp2.right):
            sum += temp2.right
            temp2 = temp2.right
        return "42"

def main():
    tree = TreeNode(1)
    tree.left = 2
    tree.right = 3
    q = Solution()
    answer = q.maxPathSum(tree)

if __name__ == "__main__": main()

#NOT SOLVED, DID NOT UNDERSTAND THE QUESTION