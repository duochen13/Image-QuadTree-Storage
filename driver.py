import imageio
from helper import print_quad_tree_iterative, print_quad_tree_recursive
from quadtree import construct_quad_tree

test_matrix_0 = [[1,1,2,3],
                 [1,1,4,5],
                 [2,2,6,6],
                 [2,2,6,6]]
# sometimes width != height, to be fixed
m, n = len(test_matrix_0), len(test_matrix_0[0])

test_quadtree_0 = construct_quad_tree(test_matrix_0, 1)
# print_quad_tree_iterative(test_quadtree_0)

img = imageio.imread('telsajoke.png')
I,J,K = img.shape # (738 1754 4)
N = min(I, J)

img_layer_0, img_layer_1, img_layer_2 = img[:,:,0], img[:,:,1], img[:,:,2]
img_layer_0 = img_layer_0[:,:N]

err = 10
img_layer_0_quadtree = construct_quad_tree(img_layer_0, err)
num_full_nodes, total_nodes = print_quad_tree_iterative(img_layer_0_quadtree)
# num_full_nodes, total_nodes, err
# 65173 87002 3
# 65108 86933 4
# 64951 86770 5
# 64489 86257 10
print(num_full_nodes, total_nodes) # 64951 86770 5
# print()

