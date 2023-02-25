class Solution:
    def reverseList(self, head):
        node = head
        prev = None
        while node!=None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

ans = Solution()
head = [1,2,3,4,5]
print(ans.reverseList(head))