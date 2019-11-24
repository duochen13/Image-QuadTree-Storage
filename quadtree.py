from helper import print_quad_tree_iterative, print_quad_tree_recursive


class QuadTree:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
    def get_childs(self):
        return [self.topLeft, self.topRight, self.bottomLeft, self.bottomRight]


def construct_quad_tree(matrix, err):
    def construct_helper(x, y, size):
        if size == 0:
            return None
        if size == 1:
            return QuadTree(matrix[x][y], True, None, None, None, None)
        size = size // 2
        tl = construct_helper(x, y, size)
        tr = construct_helper(x, y + size, size)
        bl = construct_helper(x + size, y, size)
        br = construct_helper(x + size, y + size, size)
        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and abs(tl.val - tr.val) < err and abs(tr.val - bl.val) < err and abs(bl.val -- br.val) < err:
            return QuadTree(tl.val, True, None, None, None, None)
        return QuadTree(-1, False, tl, tr, bl, br)      
    return construct_helper(0, 0, len(matrix))

def convertFromTreeToMatrix(node, size):
    pass