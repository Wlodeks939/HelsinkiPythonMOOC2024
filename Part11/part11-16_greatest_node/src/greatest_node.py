# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child



def print_nodes(root: Node):
    print(root.value)

    if root.left_child is not None:
        print_nodes(root.left_child)

    if root.right_child is not None:
        print_nodes(root.right_child)


def sum_of_nodes(root: Node):
    node_sum = root.value

    if root.left_child is not None:
        node_sum += sum_of_nodes(root.left_child)

    if root.right_child is not None:
        node_sum += sum_of_nodes(root.right_child)

    return node_sum   

def greatest_node(root: Node):
    max_node = root.value

    if root.left_child is not None:
        left_max = greatest_node(root.left_child)
        if left_max > max_node:
            max_node = left_max

    if root.right_child is not None:
        right_max = greatest_node(root.right_child)
        if right_max > max_node:
            max_node = right_max

    return max_node       
    

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    #print_nodes(tree)
    #print()
    #print(sum_of_nodes(tree))
    #print()
    print(greatest_node(tree))
