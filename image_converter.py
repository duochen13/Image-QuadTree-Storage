import imageio
import visvis as vv

img = imageio.imread('telsajoke.png')

I,J,K = img.shape
for i in range(I):
    for j in range(J):
        temp = []
        for k in range(K):
            temp.append(img[i][j][k])
        assert temp[-1] == 255
        print(temp)
print(img)
print(img.shape) # (738, 1754, 4)

