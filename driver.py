import imageio
from helper import print_quad_tree_iterative, print_quad_tree_recursive
from quadtree import construct_quad_tree, convertFromTreeToMatrix

test_matrix_0 = [[1,1,2,3],
                 [1,1,4,5],
                 [2,2,6,6],
                 [2,2,6,6]]

test_matrix_1 = [[1,1,1,1,2,2,3,3],
                 [1,1,1,1,2,2,3,3],
                 [1,1,1,1,4,4,5,5],
                 [1,1,1,1,4,4,5,5],
                 [6,6,6,6,1,2,4,4],
                 [6,6,6,6,3,4,4,4],
                 [6,6,6,6,5,5,6,6],
                 [6,6,6,6,5,5,6,6]]

# test_quadtree_1 = construct_quad_tree(test_matrix_1, 1)
# test_recover_quadtree_1 = convertFromTreeToMatrix(test_quadtree_1, size=8)
# print(test_recover_quadtree_1)



img = imageio.imread('telsajoke.png')
I,J,K = img.shape # (738 1754 4)
N = min(I, J)

img_layer_0, img_layer_1, img_layer_2 = img[:,:,0], img[:,:,1], img[:,:,2]
img_layer_0 = img_layer_0[:,:N]
img_layer_1 = img_layer_1[:,:N]
img_layer_2 = img_layer_2[:,:N]


err = 10
img_layer_0_quadtree = construct_quad_tree(img_layer_0, err)
img_layer_1_quadtree = construct_quad_tree(img_layer_1, err)
img_layer_2_quadtree = construct_quad_tree(img_layer_2, err)

img_layer_0_recover = convertFromTreeToMatrix(img_layer_0_quadtree, N)
img_layer_1_recover = convertFromTreeToMatrix(img_layer_1_quadtree, N)
img_layer_2_recover = convertFromTreeToMatrix(img_layer_2_quadtree, N)

created_img = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]
for k in range(4):
    if k == 0:
        for i in range(N):
            for j in range(N):
                created_img[i][j][k] = img_layer_0_recover[i][j]
    elif k == 1:
        for i in range(N):
            for j in range(N):
                created_img[i][j][k] = img_layer_1_recover[i][j]
    elif k == 2:
        for i in range(N):
            for j in range(N):
                created_img[i][j][k] = img_layer_2_recover[i][j]
    else:
        for i in range(N):
            for j in range(N):
                created_img[i][j][k] = 255



# num_full_nodes, total_nodes = print_quad_tree_iterative(img_layer_0_quadtree)
# num_full_nodes, total_nodes, err
# 
# 65470 87313 1
# 65173 87002 3
# 65108 86933 4
# 64951 86770 5
# 64489 86257 10
# print(num_full_nodes, total_nodes) # 64951 86770 5

