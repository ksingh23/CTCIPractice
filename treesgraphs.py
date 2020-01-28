from collections import deque
import random


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def minimal_tree(self, lst):
        if len(lst) == 0:
            return None
        elif len(lst) == 1:
            return TreeNode(lst[0])
        else:
            midpt = len(lst)//2
            node = TreeNode(lst[midpt])
            node.left = self.minimal_tree(lst[:midpt])
            node.right = self.minimal_tree(lst[midpt+1:])
            return node

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val)
            self.inorder_traversal(node.right)

    def list_of_depths(self, node):
        q = deque()
        q.append(node)
        final_list = []
        while q:
            ptr = ListNode(-1)
            head = ptr
            for i in range(len(q)):
                node = q.popleft()
                list_node = ListNode(node.val)
                ptr.next = list_node
                ptr = ptr.next
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            final_list.append(head.next)
        return final_list

    def successor(self, root, val):
        node = self.find_in_bst(root, val)
        if node.right:
            temp = node.right
            while temp.left:
                temp = temp.left
            return temp
        else:
            ancestor = root
            successor = None
            while ancestor.val != node.val:
                if ancestor.val > node.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor

    def find_in_bst(self, root, val):
        if root.val == val:
            return root
        elif root.val > val:
            return self.find_in_bst(root.left, val)
        else:
            return self.find_in_bst(root.right, val)

    def weave_lists(self, first, second, prefix, results):
        if not first or not second:
            results.append(prefix + first + second)
            return
        first_head = first[1:]
        first_prefix = first[0]
        self.weave_lists(first_head, second, prefix + [first_prefix], results)
        second_head = second[1:]
        second_prefix = second[0]
        self.weave_lists(first, second_head, prefix + [second_prefix], results)

    def bst_sequences(self, root):
        if not root:
            return [[]]
        sol = []
        prefix = [root.val]
        left = self.bst_sequences(root.left)
        right = self.bst_sequences(root.right)
        for i in range(len(left)):
            for j in range(len(right)):
                weaved = []
                self.weave_lists(left[i], right[j], prefix, weaved)
        sol += weaved
        return sol

    def insert(self, root, x):
        if not root:
            root = TreeNode(x)
        else:
            if root.val < x:
                if not root.right:
                    root.right = TreeNode(x)
                else:
                    self.insert(root.right, x)
            else:
                if not root.left:
                    root.left = TreeNode(x)
                else:
                    self.insert(root.left, x)

    def find(self, root, x):
        if not root:
            return None
        else:
            if root.val == x:
                return root
            elif root.val > x:
                return self.find(root.left, x)
            else:
                return self.find(root.right, x)

    def delete_deepest(self, root):
        temp = root
        while temp.right.right:
            temp = temp.right
        temp.right = None

    def delete(self, root, x):
        del_node = self.find(root, x)
        temp = root
        while temp.right:
            temp = temp.right
        value = temp.val
        del_node.val = value
        self.delete_deepest(root)
        return root

    def build_inorder_traversal(self, root):
        if not root:
            return []
        elif not root.right and not root.left:
            return [root.val]
        else:
            return self.build_inorder_traversal(root.left) + [root.val] + self.build_inorder_traversal(root.right)

    def get_random_node(self, root):
        lst = self.build_inorder_traversal(root)
        index = random.randrange(0, len(lst)-1)
        return lst[index]


class Graph:
    def __init__(self, length):
        self.length = length
        self.adj = []
        for i in range(length):
            self.adj.append([])

    def add_edge(self, n1, n2):
        self.adj[n1].append(n2)

    def remove_edge(self, n1, n2):
        for i in range(len(self.adj[n1])):
            if self.adj[i] == n2:
                break
        del self.adj[n1][i]

    def route_between_nodes(self, n1, n2):
        n1_visited = [False] * self.length
        n2_visited = [False] * self.length
        d1, d2 = deque(), deque()
        d1.append(n1)
        d2.append(n2)
        n1_visited[n1] = True
        n2_visited[n2] = True
        while d1 and d2:
            node1 = d1.popleft()
            node2 = d2.popleft()
            if node1 == n2 or node2 == n1:
                return True
            for n in self.adj[node1]:
                if not n1_visited[n]:
                    n1_visited[n] = True
                    d1.append(n)
            for n in self.adj[node2]:
                if not n2_visited[n]:
                    n2_visited[n] = True
                    d2.append(n)
            for i in range(self.length):
                if n1_visited[i] and n2_visited[i]:
                    return True
        return False

    def build_order(self, dependencies):
        self.add_dependencies(dependencies)
        indegree = self.get_indegree()
        build_list = []
        built = [False] * self.length
        while len(build_list) < self.length:
            poss = False
            added = 0
            i = 0
            while i < len(indegree) and not poss:
                if indegree[i] == 0 and not built[i]:
                    added = i
                    poss = True
                i += 1
            if not poss:
                return []
            build_list.append(added)
            built[added] = True
            for n in self.adj[added]:
                indegree[n] -= 1
            self.adj[added].clear()
        return build_list

    def add_dependencies(self, dependencies):
        for dep in dependencies:
            self.add_edge(dep[0], dep[1])

    def get_indegree(self):
        indegree = [0] * self.length
        for i in range(self.length):
            for n in self.adj[i]:
                indegree[n] += 1
        return indegree

    def bfs(self):
        visited = [False] * self.length
        q = deque()
        q.append(0)
        while q:
            node = q.popleft()
            print(node)
            for n in self.adj[node]:
                if not visited[n]:
                    visited[n] = True
                    q.append(n)






