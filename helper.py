def print_quad_tree_recursive(node):
    if node.isLeaf:
        print(node.val)
        return
    print_quad_tree_recursive(node.topLeft)
    print_quad_tree_recursive(node.topRight)
    print_quad_tree_recursive(node.bottomLeft)
    print_quad_tree_recursive(node.bottomRight)

def print_quad_tree_iterative(node):
    if not node:
        return
    num_full_nodes = 0
    total_nodes = 0
    q = [node]
    level = 0
    while q:
        cur_node = q.pop(0)
        total_nodes += 1
        temp = []
        for child_pos, child_node in zip(["tl","tr","bl",'br'], cur_node.get_childs()):
            if child_node.isLeaf:
                temp.append("{}: {}".format(child_pos, child_node.val))
                continue
            q.append(child_node)
        if len(temp) == 4:
            num_full_nodes += 1
        print("level:{}, nodes:{}".format(level, temp))
        level += 1
    return num_full_nodes, total_nodes