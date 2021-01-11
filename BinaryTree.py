import random
# ---------------------------------
# Code for binary trees
class BNode:
    """ Binary search tree node class"""

    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.children = [left, right]
        self.parent = parent

    def __repr__(self):
        return "Node({})".format(self.data)


class BTree:
    """ Binary tree class (storing the root node; has member functions) """

    def __init__(self, root):
        self.root = root

    def insert(self, val):
        """ insert a new leaf node with data val"""
        node = self.root
        while node:
            p = node
            side = val > node.data
            node = node.children[side]

        p.children[side] = BNode(val, None, None, p)  # new leaf, parent p

    def find(self, val):
        """ find a node with data val """
        n = self.root
        while n and n.data != val:
            n = n.children[val > n.data]

        return n  # returns None if not found

    def remove(self, val):
        """ removes a node with data val """
        n = self.find(val)
        if not n:
            print(f"node ({val}) not found!")
            return
        else:
            self.delete(n)

    def delete(self, n):
        """ deletes the specified node (must be in the tree)"""
        left = n.children[0]
        right = n.children[1]

        print(f"Call: delete({n})")
        # Case: If the node has two children ...
        if left and right:
            while left.children[1]:  # find largest predecessor
                left = left.children[1]

            print(f"> move {left} into {n}")
            n.data = left.data  # move up the predecessor
            self.delete(left)  # ... recursively remove old node
            return

        # Case: leaf node
        if not(left or right):
            if n == self.root:
                self.root = None
            else:
                side = n.data > n.parent.data
                n.parent.children[side] = None  # cut off the node
                print("- remove leaf")
            return

        # Case: one child... first get the child...
        if left:
            child = left
        else:
            child = right

        # ...then delete.
        if n == self.root:
            self.root = child
            child.parent = None
        else:
            side = n.data > n.parent.data
            n.parent.children[side] = child
            child.parent = n.parent
            print("- remove (one side)")

        return  # nothing to return, but could have a return code for success

    def __repr__(self):
        """crude print for the tree, with each depth on one line.
           Uses * to denote None (no child for a node)"""
        level = 0
        q = [(self.root, level)]
        rep = ""
        while q:
            n, level = q.pop(0)
            if not n:
                rep += "*"
            else:
                rep += str(n.data)
                q.append((n.children[0], level+1))
                q.append((n.children[1], level+1))
            rep += " "
            if q and q[0][1] > level:
                rep += "\n"

        return rep

def leaves(root):
    
    if root:
            
        left_child = root.children[0]
        right_child = root.children[1]

        if left_child or right_child:
            all_leaves = leaves(left_child) + leaves(right_child)
            return all_leaves

        else: #if there are no leaves
            return root

    else: #if input is not a root
        return[]


def depth(root):
    
    if root:

        left_child = root.children[0]
        right_child = root.children[1]

        net_depth = max(depth(left_child), depth(right_child)) +1

        return net_depth #maximum depth between left and right, +1 bc root itself counts

    else: #if there is no root, depth=0
        return 0

if __name__ == '__main__':

    #test tree 
    test_tree = BTree(BNode(100))
    [test_tree.insert(random.randint(1,1000)) for i in range(100)]

    print(test_tree)



    