import cv2
 
# Read the original image
img = cv2.imread('./test_images/NJIT_logo.png') 

# Display original image
cv2.imshow('Original', img)
 
# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
 
# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection

# Allows for smoother edges
smoothed_edges = cv2.GaussianBlur(edges, (5, 5), 0)  # Smooth the edges

# More pointy
# smoothed_edges = cv2.bilateralFilter(edges, 9, 75, 75)

# Display the smoothed Canny Edge Detection Image
cv2.imshow('Smoothed Canny Edge Detection', smoothed_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
