import matplotlib.pyplot as plt
import numpy as np


def trap(height):
	n = len(height)
	if n == 0:
		return 0

	left_max = [0] * n
	right_max = [0] * n

	left_max[0] = height[0]
	for i in range(1, n):
		left_max[i] = max(left_max[i - 1], height[i])

	right_max[n - 1] = height[n - 1]
	for i in range(n - 2, -1, -1):
		right_max[i] = max(right_max[i + 1], height[i])

	trapped_water = [0] * n
	for i in range(n):
		trapped_water[i] = min(left_max[i], right_max[i]) - height[i]

	return trapped_water


def visualize(height, water):
	max_height = max(height)
	width = len(height)
	visualization = np.zeros((max_height + 1, width, 3), dtype=np.uint8)

	for i, h in enumerate(height):
		visualization[:h, i] = [0, 0, 0]  # Elevation Map (black)

	for i in range(len(height)):
		start = max_height - water[i]
		visualization[start:max_height, i] = [0, 0, 255]  # Trapped Water (blue)

	# Display the visualization
	plt.imshow(visualization)
	plt.axis('off')
	plt.show()


elevation_map = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
trapped_water = trap(elevation_map)

visualize(elevation_map, trapped_water)
