"""
单链表的实现
https://www.cnblogs.com/yudanqu/p/9172459.html

双端链表
deque是栈和队列的一种广义实现，deque是"double-end queue"的简称；deque支持线程安全、
有效内存地以近似O(1)的性能在deque的两端插入和删除元素，尽管list也支持相似的操作，但是
它主要在固定长度操作上的优化，从而在pop(0)和insert(0,v)（会改变数据的位置和大小）上有O(n)的时间复杂度。
https://blog.csdn.net/chl183/article/details/106958004

deque()
append()
appendleft()
extend()
extendleft()
pop()
popleft()
count()
insert(index,obj)
rotate(n)
clear()
remove()
maxlen

"""
# deque栈和队列的一种广义实现
# from collections import deque


# 栈的实现如下
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        # self.dq = collections.deque([])
        self.top = None

    def peek(self):
        if self.top is not None:
            return self.top.value
        else:
            return None

    def push(self, n):
        node = Node(n)
        node.next = self.top
        self.top = node
        return node.value

    def pop(self):
        if self.top is not None:
            tmp = self.top.value
            self.top = self.top.next
        else:
            return None
        return tmp

if __name__ == "__main__":
    nums = [1,2,3,4]
    stack_test = Stack()
    print(stack_test.pop())
    print(stack_test.push(12))
    print(stack_test.push(14))
    print(stack_test.push(16))
    print(stack_test.push(18))
    print(stack_test.pop())
    print(stack_test.pop())
    print(stack_test.pop())
    print(stack_test.pop())
    print(stack_test.pop())