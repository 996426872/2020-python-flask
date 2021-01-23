# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         i = 0
#         total_val = l1.val
#         while l1.next != None:
#             i = i + 1
#             total_val = total_val + (l1.val * (10 ** i))
#             l1 = l1.next
#
#         i = 0
#         total_val = total_val + l2.val
#         while l2.next != None:
#             i = i + 1
#             total_val = total_val + (l2.val * (10 ** i))
#             l2 = l2.next
#         print ("total_val=%d" % total_val)
#         root = None
#         node_pre = None
#         for num in str(total_val)[::-1]:
#             if root == None:
#                 root = ListNode (eval (num))
#                 node_pre = root
#             else:
#                 node = ListNode (num)
#                 node_pre.next = node
#                 node_pre = node
#         return root



class Solution:
    def addTwoNumbers(self, l1, l2):
        total_val = 0
        for i in range(0, len(l1)):
            print("total_val=%d" % total_val)
            total_val = total_val + (l1[i] * (10 ** i))

        for i in range(0, len(l2)):
            print ("total_val=%d" % total_val)
            total_val = total_val + (l2[i] * (10 ** i))

        print("total_val=%d" % total_val)
        nums = []
        for num in str(total_val)[::-1]:
            nums.append(eval(num))
        return nums

if __name__ == "__main__":
    # 输入：l1 = [9 , 9 , 9 , 9 , 9 , 9 , 9] , l2 = [9 , 9 , 9 , 9]
    # 输出：[8 , 9 , 9 , 9 , 0 , 0 , 0 , 1]
    l1 = [9 , 9 , 9 , 9 , 9 , 9 , 9]
    l2 = [9 , 9 , 9 , 9]
    solu = Solution()
    print(solu.addTwoNumbers(l1,l2))