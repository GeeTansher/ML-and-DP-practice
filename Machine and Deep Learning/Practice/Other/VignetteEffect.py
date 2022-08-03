import cv2
import numpy as np

img = cv2.imread('./images/cat.jpeg')
rows, cols = img.shape[:2]

# Generating two kernels because image can be rectangle to fully cover it
kernel_x = cv2.getGaussianKernel(rows, 200)
kernel_y = cv2.getGaussianKernel(cols, 200)
# Single kernel of size = (rows x cols)
kernel = kernel_x * kernel_y.T

# Normalize it
kernel = kernel/np.linalg.norm(kernel)

# After norm. values will be quite low so to level it
mask = 255 * kernel
output = np.copy(img)

# Applying mask to every color channel
for i in range(3):
    output[:,:,i] = output[:,:,i] * mask

cv2.imshow("original",img)
cv2.imshow("Vignette", output)
cv2.waitKey()
cv2.destroyAllWindows()
