import json
from typing import Optional
from tree_node import TreeNode
from dataclasses_json import dataclass_json
from dataclasses import dataclass


@dataclass_json
@dataclass
class MySearchBinaryTree:
    count: int = 0
    root: Optional[TreeNode] = None

    def insert(self, value):
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value > current_node.value:
                    if not current_node.right:
                        current_node.right = new_node
                        break
                    current_node = current_node.right
                elif value < current_node.value:
                    if not current_node.left:
                        current_node.left = new_node
                        break
                    current_node = current_node.left

        self.count += 1

    def lookup(self, value):
        if not self.root:
            return None

        current_node = self.root
        while current_node:
            if current_node.value == value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right

        return None

    def remove(self, value):
        # 1. If node_to_remove is a leaf node then remove it by detaching it from its parent.
        # 2. If node_to_remove has only one child then replace it with its only child node, which will preserve the BST value ordering.
        # 3. If node_to_remove has two children then find the successor node and replace with it.
        node_to_remove, parent_node, is_left_child = self.find_node_and_parent_and_position(value)
        if not node_to_remove:
            return

        if not node_to_remove.left and not node_to_remove.right:
            self.replace_node(parent_node, is_left_child, None)

        elif node_to_remove.left and node_to_remove.right:
            successor_node = self.find_and_detach_and_get_successor_node(node_to_remove)
            successor_node.left = node_to_remove.left
            successor_node.right = node_to_remove.right
            self.replace_node(parent_node, is_left_child, successor_node)

        else:
            if node_to_remove.left:
                self.replace_node(parent_node, is_left_child, node_to_remove.left)
            elif node_to_remove.right:
                self.replace_node(parent_node, is_left_child, node_to_remove.right)

    def replace_node(self, parent_node, is_left, replacement_node):
        if not parent_node:  # if there is no parent node then it must be the root node.
            replacement_node.left = self.root.left
            replacement_node.right = self.root.right
            self.root = replacement_node
            return

        if is_left:
            parent_node.left = replacement_node
        else:
            parent_node.right = replacement_node

    def find_node_and_parent_and_position(self, value):
        if not self.root:
            return None

        current_node = self.root
        parent_node = None
        is_left_child = False
        while current_node:
            if current_node.value == value:
                return current_node, parent_node, is_left_child
            elif value < current_node.value:
                is_left_child = True
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                is_left_child = False
                parent_node = current_node
                current_node = current_node.right

        return None

    @staticmethod
    def find_and_detach_and_get_successor_node(node_to_remove):
        # 1. Check if node_to_remove has a right child, and choose successor as the "lowest left child" in the node_to_remove's right child's subtree.
        #   1. If so then check if the right child has a left child.
        #       1. If so then choose the lowest left child in the left subtree as successor by traversing to the leaf node.
        #       2. Detach the successor node from its current parent node.
        #   2. If not then choose the right child as the successor.
        # 2. This is because the lowest left child in the right child's subtree will be,
        #   1. Greater than all nodes of node_to_remove left subtree.
        #   2. Less than all nodes of node_to_remove right subtree.
        #   3. Replacing it with successor will preserve the BST value ordering.

        removing_node_right_child = node_to_remove.right
        if not removing_node_right_child.left:
            return removing_node_right_child

        current_left_node = removing_node_right_child.left
        current_left_node_parent = removing_node_right_child
        while current_left_node.left:
            current_left_node_parent = current_left_node
            current_left_node = current_left_node.left
        else:
            current_left_node_parent.left = None
            return current_left_node

    def __str__(self):
        return str(self.root)
        # return self.root.to_json()
        # return json.dumps(json.loads(self.root.to_json()), indent=2)


bst = MySearchBinaryTree()
# bst.insert(9)
# bst.insert(4)
# bst.insert(6)
# bst.insert(20)
# bst.insert(170)

bst.insert(71)
bst.insert(74)
bst.insert(10)
bst.insert(85)
bst.insert(53)
bst.insert(36)
bst.insert(82)
bst.insert(84)

# print(str(bst.lookup(53)))

bst.remove(74)
bst.remove(82)
bst.remove(71)

print(bst.__str__())
