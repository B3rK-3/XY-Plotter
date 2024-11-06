
import turtle
from PIL import Image

def draw_image(image_path):
    # Open and convert the image to grayscale
    img = Image.open(image_path).convert("L")

    # Resize the image (optional)
    img = img.resize((100, 100))

    # Create a Turtle object
    t = turtle.Turtle()
    t.speed(0)  # Set the fastest drawing speed

    # Iterate through the pixels
    for y in range(img.height):
        for x in range(img.width):
            pixel_value = img.getpixel((x, y))

            # Draw a dot if the pixel is dark enough
            if pixel_value < 128:
                t.penup()
                t.goto(x - img.width // 2, img.height // 2 - y)
                t.pendown()
                t.dot()

    turtle.done()

# Example usage
#draw_image("./web/imgs/NJIT-LOGO.jpg") 


'''
import turtle
from PIL import Image

def draw_image_from_path(image_path, pixel_path):
    """Draws an image using turtle, following a given pixel path."""

    # Open the image
    img = Image.open(image_path)

    # Create a turtle object
    t = turtle.Turtle()
    t.speed(0)  # Set the fastest drawing speed

    # Iterate through the pixel path
    for x, y in pixel_path:
        # Get the pixel color at the given coordinates
        color = img.getpixel((x, y))

        # Set the turtle's pen color
        t.pencolor(color)

        # Move the turtle to the pixel's position
        t.penup()
        t.goto(x, y)
        t.pendown()

        # Draw a dot representing the pixel
        t.dot(1)

    turtle.done()

# Example usage:
image_path = "./web/imgs/NJIT-LOGO.jpg"  # Replace with your image path
pixel_path = path  # Replace with your pixel path

draw_image_from_path(image_path, pixel_path)
'''

