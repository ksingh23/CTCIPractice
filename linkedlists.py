from collections import defaultdict


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeDups(head):
    d = defaultdict(bool)
    temp = head
    prev = None
    while temp:
        if not d[temp.val]:
            d[temp.val] = True
        else:
            prev.next = temp.next
        prev = temp
        temp = temp.next
    return head


def kthtolast(head, k):
    fast, slow = head, head
    i = 0
    while i < k:
        slow = slow.next
        i += 1
    while slow:
        fast = fast.next
        slow = slow.next
    return fast


def deleteMiddleNode(middle):
    dummy = middle.next
    middle.val = dummy.val
    middle.next = dummy.next


def partition(head, x):
    small = None
    smallHead = None
    large = None
    largeHead = None
    temp = head
    while temp:
        if temp.val < x:
            node = Node(temp.val)
            if not small:
                small = node
                smallHead = node
            else:
                small.next = node
                small = small.next
        else:
            node = Node(temp.val)
            if not large:
                large = node
                largeHead = node
            else:
                large.next = node
                large = large.next
        temp = temp.next
    small.next = largeHead
    head = smallHead
    return head


def sumLists(h1, h2):
    temp1, temp2 = h1, h2
    sumHead = None
    sumTrav = None
    carry = 0
    while temp1 and temp2:
        sum = temp1.val + temp2.val
        if carry == 1:
            sum += 1
        node = Node((sum % 10))
        if sum >= 10:
            carry = 1
        else:
            carry = 0
        if not sumHead:
            sumHead = node
            sumTrav = node
        else:
            sumTrav.next = node
            sumTrav = sumTrav.next
        temp1 = temp1.next
        temp2 = temp2.next
    return sumHead


def palindrome(head):
    rev = reverse(head)
    temp = head
    temp1 = rev
    while temp:
        if temp.val != temp1.val:
            return False
        temp = temp.next
        temp1 = temp1.next
    return True


def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head


