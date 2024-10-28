import cv2
import numpy as np
from collections import deque


class xy_image:
    def __init__(self):
        # Read the original image
        self.img = cv2.imread("./web/upload_img/img.png")

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
        img = edges  # Smooth the edges

        # convert to bool array to decrease runtime
        self.array = np.array(img, dtype=bool)

        cv2.imwrite("./web/export_img/export.png", img)

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

    def findWhite(self, r, c):
        # function to find a white pixel in the image given a point
        for i in range(r, len(self.array)):
            for j in range(c, len(self.array[0])):
                if self.array[i][j]:
                    self.array[i][j] = False
                    return (i, j)
        return [-1, -1]

    def findPath(self):
        # create a path which the robot will follow
        path = []
        # double ended list
        q = deque()
        r, c = 0, 0  # initialize a point that we can continue searching for points from
        first = self.findWhite(r, c)  # find first point
        r, c = first  # set the point to the newly found to continue from there
        # append first white to queue and path
        q.append(first)
        path.append(first)

        # performance testing ---
        # start = time.time()

        whites = self.white

        while len(path) != whites:
            # if queue has elements we should continue finding from there
            if q:
                node = q.popleft()
                path.append(node)
                q.extend(self.search(node[0], node[1]))
            else:
                # if queue is exahusted find new point
                p = self.findWhite(r, c)
                r, c = p
                q.append(p)
                path.append(p)
        # performance testing ---
        # end = time.time()
        return path


class write_img:
    def __init__(self, path):
        data = None
        with open(path, "rb") as file:
            data = file.read()
        with open("./web/upload_img/img.png", "wb") as file:
            file.write(data)
