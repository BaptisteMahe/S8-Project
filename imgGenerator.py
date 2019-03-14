from PIL import Image, ImageDraw
from random import randrange
from time import time

# base variables

size = 100
resolution = 10
num = int(size / resolution)
grid = []

# generating a random grid
t = time()

grid = [[randrange(0, 2) for i in range(0, num)] for j in range(0, num)]
# set up the drawing

img = Image.new('RGB', (size, size), 'white')
draw = ImageDraw.Draw(img)

# draw a black rectangle for every 1 in the grid

for i in range(0, num):
    for j in range(0, num):
        if grid[i][j] == 1:
            x0, y0 = i * resolution, j * resolution
            x1, y1 = (i + 1) * resolution, (j + 1) * resolution
            draw.rectangle([x0, y0, x1, y1], fill='black')

# name and save the result

filename = "pil_img.png"
img.save(filename)

print(time() - t)
