import cv2
import numpy as np


class xy_image:
    def __init__(self, path):
        # Read the original image
        self.img = cv2.imread("./test_images/" + path)

    def detect_edge(self):
        # Convert to grayscale
        self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # Blur the image for better edge detection
        self.img_blur = cv2.GaussianBlur(self.img_gray, (3, 3), 0)

        # Canny Edge Detection
        edges = cv2.Canny(
            image=self.img_blur, threshold1=100, threshold2=200
        )  # Canny Edge Detection

        # Allows for smoother edges
        self.array = np.array(
            cv2.GaussianBlur(edges, (5, 5), 0), dtype=bool
        )  # Smooth the edges

        self.white = self.array.sum()

    def search(self, y, x):
        rows, cols = self.array.shape
        found = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Adjacent cells only

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and self.array[ny, nx]:
                found.append((ny, nx))
                self.array[ny, nx] = False  # Mark as visited

        return found

    def find(self, r, c):
        # function to find a white pixel in the image given a point
        for i in range(r, len(self.array)):
            for j in range(c, len(self.array[0])):
                if self.array[i][j]:
                    self.array[i][j] = False
                    return (i, j)
        return [-1, -1]
