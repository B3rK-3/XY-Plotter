import cv2
from collections import deque

class xy_image:
    def __init__(self, base):
        # Read the original image
        self.img = cv2.imread("./web/upload_img/img.jpg")

    def detect_edge(self, h, w, blur_ksize=5, canny_threshold1=40, canny_threshold2=170):
        if h and w:        
            self.img = cv2.resize(self.img, (int(w), int(h)))

        # Convert to grayscale
        img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur for smoother edges
        img_blur = cv2.GaussianBlur(img_gray, (blur_ksize, blur_ksize), 0)

        # Perform Canny edge detection
        self.array = cv2.Canny(img_blur, canny_threshold1, canny_threshold2)
    
    
        cv2.imwrite("./web/export_img/export.jpg", self.array)

    def search(self, y, x):
        rows, cols = self.array.shape[:2]
        found = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Adjacent cells only

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and self.array[ny, nx] >= self.base:
                found.append((ny, nx))
                self.array[ny, nx] = 0  # Mark as visited

        return found

    def findWhite(self, r, c):
        # Function to find a white pixel in the image starting from point (r, c)
        rows, cols = self.array.shape[:2]
        # Start searching from the given point
        for i in range(r, rows):
            for j in range(c if i == r else 0, cols):
                if self.array[i, j] >= self.base:
                    self.array[i, j] = 0
                    return (i, j)
        # If not found, wrap around and start from the beginning up to the starting point
        for i in range(0, r):
            for j in range(0, cols):
                if self.array[i, j] >= self.base:
                    self.array[i, j] = 0
                    return (i, j)
        # If no white pixel is found, return [-1, -1]
        return [-1, -1]

    def findPath(self):
        # create a path which the robot will follow
        path = []
        # double ended list
        q = deque()
        r, c = 0, 0  # initialize a point that we can continue searching for points from
        found = self.findWhite(r, c)  # find first point
        r, c = found  # set the point to the newly found to continue from there
        # append first white to queue and path
        q.append(found)
        path.append(found)

        # performance testing ---
        # start = time.time()

        while found != [-1,-1]:
            # if queue has elements we should continue finding from there
            if q:
                node = q.popleft()
                path.append(node)
                q.extend(self.search(node[0], node[1]))
            else:
                path.append((None, None)) # a break like sequence added to path indicating that the pen should be lifted
                # if queue is exahusted find new point
                found = self.findWhite(r, c)
                r, c = found
                q.append(found)
        # performance testing ---
        # end = time.time()
        return path


class write_img:
    def __init__(self, path):
        data = None
        with open(path, "rb") as file:
            data = file.read()
        with open("./web/upload_img/img.jpg", "wb") as file:
            file.write(data)
