class Solution:
    def searchBST(self, root,val):
        if root == None:
            return
        if root.val==val:
            return root
        if root.val<val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)

ans = Solution()
root = [4, 2, 7, 1, 3]
val = 5
print(ans.searchBST(root,val))