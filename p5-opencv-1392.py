import cv2

# Read the image from file
image = cv2.imread('carrorojo.jpeg')
# Display the image in a window
cv2.imshow('Carro rojo Daniel Gallegos 1392', image)
# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load the image
image = cv2.imread('carrorojo.jpeg')
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Save the grayscale image
cv2.imwrite('carro_gris.jpeg', gray_image)

# Load the image
image = cv2.imread('carrorojo.jpeg')
# Resize the image to 300x200
resized_image = cv2.resize(image, (300, 200))
# Save the resized image
cv2.imwrite('imagen_redimensionada Daniel Gallegos 1392.jpeg', resized_image)

# Load the image
image = cv2.imread('carrorojo.jpeg')
# Get the image's height and width
(h, w) = image.shape[:2]
# Define the center of the image
center = (w // 2, h // 2)
# Rotation matrix
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
# Perform the rotation
rotated_image = cv2.warpAffine(image, matrix, (w, h))
# Save the rotated image
cv2.imwrite('imagen_rotada Daniel Gallegos 1392.jpg', rotated_image)

# Load the image
image = cv2.imread('carrorojo.jpeg')
# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
# Save the blurred image
cv2.imwrite('imagen_borrosa Daniel Gallegos 1392.jpg', blurred_image)

# Load the image
image = cv2.imread('carrorojo.jpeg')
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply Canny edge detector
edges = cv2.Canny(gray_image, 100, 200)
# Save the edges image
cv2.imwrite('bordes Daniel Gallegos 1392.jpeg', edges)

# Load the image
image = cv2.imread('carrorojo.jpeg')
# Draw a rectangle
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 3)
# Add text to the image
cv2.putText(image, 'OpenCV', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# Save the output image
cv2.imwrite('imagen_producida Daniel Gallegos 1392.jpeg', image)

# Load the image
image = cv2.imread('carrorojo.jpeg')
# Apply thresholding
_, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# Save the thresholded image
cv2.imwrite('imagen_umbralizada Daniel Gallegos 1392.jpeg', thresh_image)

# Load the image
image = cv2.imread('carrorojo.jpeg')
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Find edges
edges = cv2.Canny(gray_image, 100, 200)
# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# Save the output image with contours
cv2.imwrite('imagen_contornos Daniel Gallegos 1392.jpeg', image)