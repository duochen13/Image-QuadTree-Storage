import imageio
from PIL import Image
import numpy as np
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


err = 0
img_layer_0_quadtree = construct_quad_tree(img_layer_0, err)
img_layer_1_quadtree = construct_quad_tree(img_layer_1, err)
img_layer_2_quadtree = construct_quad_tree(img_layer_2, err)

img_layer_0_recover = convertFromTreeToMatrix(img_layer_0_quadtree, N)
img_layer_1_recover = convertFromTreeToMatrix(img_layer_1_quadtree, N)
img_layer_2_recover = convertFromTreeToMatrix(img_layer_2_quadtree, N)

created_img = [[[255 for _ in range(3)] for _ in range(N)] for _ in range(N)]
for k in range(3):
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
    # else:
    #     for i in range(N):
    #         for j in range(N):
    #             created_img[i][j][k] = 255

# print("first row layer====")
# print(img_layer_0[0][:20])
# print("=================")
# print(img_layer_0_recover[0][:20])

data_np = np.asarray(created_img)
actual_img = Image.fromarray(data_np, 'RGB')
# actual_img = Image.fromarray(np.asarray(img[:,:,:3]), 'RGB')
actual_img.save('telsajoke_recover.png')
actual_img.show()

