import numpy as np

width = 704
height = 416
confidence = 0.55

image_np_global = np.zeros([width, height, 3], dtype=np.uint8)
depth_np_global = np.zeros([width, height, 4], dtype=np.float)
print(depth_np_global)