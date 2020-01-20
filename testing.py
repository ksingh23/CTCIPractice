import stringsarrays
import linkedlists as ll
from stacksqueues import Stack, StackNode, SetOfStacks, MyQueue, SortStack


def main():
    # print(stringsarrays.zeroMatrix([[1,2,3,0],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
    lst = [3, 5, 8, 5, 10, 2, 1]
    dummyRoot = ll.Node(-1)
    ptr = dummyRoot
    for num in lst:
        ptr.next = ll.Node(num)
        ptr = ptr.next
    ptr = dummyRoot.next
    i = 0
    temp = ptr
    while i < 2:
        temp = temp.next
        i += 1
    # ans = ll.removeDups(temp)
    # temp = ans
    # ll.deleteMiddleNode(temp)
    ptr = ll.partition(ptr, 5)
    '''
    temp = ptr
    while temp:
        print(temp.val)
        temp = temp.next
    '''
    # print(ll.kthtolast(ptr, 2).val)
    num1 = [7,1,6]
    num2 = [5,9,2]
    dummyRoot1 = ll.Node(-1)
    head1 = dummyRoot1
    for num in num1:
        head1.next = ll.Node(num)
        head1 = head1.next
    head1 = dummyRoot1.next
    dummyRoot2 = ll.Node(-1)
    head2 = dummyRoot2
    for num in num2:
        head2.next = ll.Node(num)
        head2 = head2.next
    head2 = dummyRoot2.next
    # print(ll.palindrome(ptr))
    '''
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(-1)
    # s.print_stack()
    print (s.get_min())
    s.pop()
    # s.print_stack()
    print (s.get_min())
    '''
    '''
    ss = SetOfStacks()
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(6)
    print (len(ss.stack_list))
    ss.pop()
    print (len(ss.stack_list))
    '''
    '''
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print (q.head)
    print (q.tail)
    q.pop()
    print (q.head)
    print (q.tail)
    '''
    '''
    sor = SortStack()
    sor.push(3)
    sor.s2.print_stack()
    print("End")
    sor.push(1)
    sor.s2.print_stack()
    print("End")
    sor.push(4)
    sor.s2.print_stack()
    '''



main()